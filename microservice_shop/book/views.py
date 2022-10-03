from django.views.generic import ListView, DetailView
from book.models import Book
from book.tasks import leftinstock_sync
import requests

class BookDetailView(DetailView):
    """
    Generic class-based view for a list of all books available at Dummy shop.
    """
    model = Book


class BookListView(ListView):
    """
    Generic class-based view for a list of all books available at Dummy shop.
    """
    model = Book
    paginate_by = 5

    def task(self): # todo: this does not occure
        url = "http://admin:admin@storage:8000/book/books/"
        response = requests.get(url=url)
        print(response.text)
        leftinstock_sync.delay

    def get_queryset(self):
        """
        Return list of all Book objects
        """
        queryset = Book.objects.all()
        return queryset
