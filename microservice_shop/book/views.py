from django.views.generic import ListView, DetailView
from book.models import Book
from book.tasks import leftinstock_sync_task
from order.tasks import order_status_update


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

    def get_queryset(self):
        """
        Return list of all Book objects
        """
        leftinstock_sync_task.delay()
        order_status_update.delay()
        queryset = Book.objects.all()
        return queryset
