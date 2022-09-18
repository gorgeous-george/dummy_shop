from django.contrib import admin
from book.models import Book, BookItem


class BookInline(admin.TabularInline):
    """
    Inline Model representing book copies of a particular book
    """
    model = BookItem
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin Model representing a Book as real book object stored at "storage".
    """
    inlines = [BookInline, ]
    list_display = ["title", "left_in_stock"]
    list_filter = ["title", "left_in_stock"]

    def get_queryset(self, request):
        """
        function for returning the Model queryset
        """
        return super(BookAdmin, self).get_queryset(request)
