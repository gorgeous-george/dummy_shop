# from celery import shared_task
# from django.core.mail import send_mail
#
#
# @shared_task
# def place_order(pk):
    # shop_order = Order.objects.get(id=pk)
    # API POST REQUEST to create storage's Order

    # placed_order.create(
    # client_email = shop_order.client.email,
    # status = "IN_WORK",
    # delivery_address = shop_order.delivery_address,
    # shop_order_id = shop_order.id
    # )

    # storage
    # order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    # book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)
    # book_item = models.ManyToManyField(BookItem, related_name="order_item", related_query_name="order_item")
    #
    # shop
    # order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    # book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)


# @shared_task
# def order_status_update(pk):
    # shop_order = Order.objects.get(id=pk)
    # API GET REQUEST to receive storage's Order
    # shop_order.update(status=storage_order.status)
    # if storage_order.status="SUCCESS":
    #     send_mail(
    #         'Your order has been completed',
    #         'Dear customer. Your order has been completed',
    #         'dummy_shop@dummy.com',
    #         [storage_order.client_email],
    #         fail_silently=False,
    #     )