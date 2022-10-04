from book.models import Book
from order.models import Order, OrderItem
from celery import shared_task
from django.core.mail import send_mail
import json
import requests

@shared_task
def place_order_task(pk):
    """
    posting Order into storage
    """
    shop_order = Order.objects.get(id=pk)
    order_url = "http://admin:admin@storage:8000/order/order/"
    data_for_json = {
        "client_email" : shop_order.client.email,
        "status" : "IN_WORK",
        "delivery_address" : shop_order.delivery_address,
        "shop_order_id" : pk,
        }
    converted_to_json = json.dumps(data_for_json)
    requests.post(url=order_url, json=converted_to_json)
    """
    posting Order items into storage
    """
    storage_orders = requests.get(url=order_url)
    order_items = OrderItem.objects.filter(order_id=pk)
    order_item_url = "http://admin:admin@storage:8000/order/orderitems/"
    for storage_order in storage_orders.json():
        if storage_order["shop_order_id"]==pk:
            for order_item in order_items:
                storage_order_id = storage_order["id"]
                storage_book_id = order_item.book_id
                storage_quantity = order_item.quantity
                data_for_json = {
                    "order_id": storage_order_id,
                    "book_id": storage_book_id,
                    "quantity": storage_quantity,
                    "book_item": [1],
                }
                converted_to_json = json.dumps(data_for_json)
                requests.post(url=order_item_url, json=converted_to_json)

@shared_task
def order_status_update():
    order_url = "http://admin:admin@storage:8000/order/order/"
    response = requests.get(url=order_url)
    for order in response.json():
        if order["status"]=="SUCCESS":
            shop_order = Order.objects.get(id=order["shop_order_id"])
            shop_order.update(status="SUCCESS")
            shop_order.save()
            send_mail(
                'Your order has been completed',
                'Dear customer. Your order has been completed',
                'dummy_shop@dummy.com',
                [order["client_email"]],
                fail_silently=False,
            )
