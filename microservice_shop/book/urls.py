from django.urls import path

from book.views import BookDetailView, BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='shop_books'),                               # page showing all books
    path('book_details/<int:pk>', BookDetailView.as_view(), name='shop_book_detail'),  # specific book detailed page
    ]