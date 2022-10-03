from rest_framework import permissions
from rest_framework import viewsets

from book.models import Book, BookItem
from book.serializers import BookSerializer, BookItemSerializer

from order.models import Order, OrderItem


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Book.objects.all()
        for obj in queryset:
            available_book_items = BookItem.objects.filter(book_id=obj.pk, status="AVAILABLE").count()
            obj.left_in_stock = available_book_items
            obj.save()
        return(queryset)


class BookItemViewSet(viewsets.ModelViewSet):
    serializer_class = BookItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = BookItem.objects.all()
        for obj in queryset:
            orderitems = OrderItem.objects.filter(book_id=obj.book_id, order_id__status="SUCCESS")
            for orderitem in orderitems:
                if obj.book_id == orderitem.book_id:
                    obj.status = "ORDERED"
                    obj.save()
        return(queryset)

