from django.views.generic import ListView, DetailView
from book.models import Book


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
        queryset = Book.objects.all()
        return queryset
