from django.db import models
from book.models import Book, BookItem


class Order(models.Model):
    """
    Model representing an Order created by user via web-front layer and sent from "shop" to "storage" to wrap it up
    "client_email", "delivery address" and "shop_order_id" are received from "shop"
    """
    client_email = models.EmailField(max_length=255)
    IN_WORK = 'IN_WORK'
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    STATUS_CHOICES = [
        (IN_WORK, 'In work'),
        (SUCCESS, 'Success'),
        (FAIL, 'Fail'),
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=IN_WORK)
    delivery_address = models.CharField(max_length=255)
    shop_order_id = models.IntegerField(null=True)

    class Meta:
        ordering = ["client_email", "id", "status"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.status)


class OrderItem(models.Model):
    """
    Model representing an Order items, namely a list of unique book copies required to satisfy the order.
    Order items are created based on books ids and required quantity received from "shop"
    """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    book_item = models.ManyToManyField(BookItem, related_name="order_items", related_query_name="order_item")
    # todo: while creating new OrderItem object to have a check that related BookItem.status == AVAILABLE

    class Meta:
        ordering = ["order_id", "book_id", "quantity"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.book_item)
