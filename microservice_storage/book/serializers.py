from book.models import Book, BookItem
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    """
    class Meta:
        model = Book
        fields = ['pk', 'title', 'left_in_stock']


class BookItemSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    """
    Serializer for BookItem model.
    """
    class Meta:
        model = BookItem
        fields = ['isbn', 'status', 'book_id']
