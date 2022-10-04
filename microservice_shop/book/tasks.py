from book.models import Book
from celery import shared_task
import requests


@shared_task
def test(x, y):
    return x + y


@shared_task
def leftinstock_sync_task():
    url = "http://admin:admin@storage:8000/book/books/"
    response = requests.get(url=url)
    shop_books = Book.objects.get_all()
    for storage_book in response.json():
        for shop_book in shop_books:
            if shop_book.storage_book_id == storage_book["pk"]:
                shop_book.update(left_in_stock=storage_book["left_in_stock"])
                shop_book.save()

