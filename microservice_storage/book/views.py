from rest_framework import permissions
from rest_framework import viewsets

from book.models import Book, BookItem
from book.serializers import BookSerializer, BookItemSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
