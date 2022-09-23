from django.db import models
from django.urls import reverse

from book.models import Book, User


class Order(models.Model):      # todo: to make Order.id synchronized with storage's Order.shop_order_id
    """
    Model representing an Order created by user via web-front layer.
    Simultaneously this model represents a Shopping Cart at web-from layer
    """
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    CART = 'CART'
    ORDERED = 'ORDERED'
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    STATUS_CHOICES = [          # todo: to develop API link to Storage to update this field appropriately
        (CART, 'Cart'),
        (ORDERED, 'Ordered'),
        (SUCCESS, 'Success'),
        (FAIL, 'Fail'),
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=CART)
    delivery_address = models.CharField(max_length=255)

    class Meta:
        ordering = ["client", "id", "status"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.id)

    def get_absolute_url(self):
        return reverse('shop_books')



class OrderItem(models.Model):
    """
    Model representing an Order items, namely a desired books and their quantity that the Client selected and added to the Shopping Cart
    """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)   #  todo: while creating new OrderItem object to have a check that OrderItem.quantity <= Book.left_in_stock

    def get_absolute_url(self):
        return reverse('shop_books')
