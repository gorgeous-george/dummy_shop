from django.contrib import admin
from book.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin Model representing a Book as marketing object showed to users via web-front layer.
    """
    list_display = ["title", "description", "author", "genre", "price", "left_in_stock", "storage_book_id"]
    list_filter = ["author", "genre"]

    def get_queryset(self, request):
        """
        function for returning the Model queryset
        """
        return super(BookAdmin, self).get_queryset(request)
