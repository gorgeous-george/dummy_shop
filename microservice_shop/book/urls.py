from django.urls import path


urlpatterns = [
    path('index/', BookListView.as_view(), name='shop_books'),                      # main page with all books
    path('index/book_details', BookDetailView.as_view(), name='shop_book_detail'),  # specific book detailed page
    ]