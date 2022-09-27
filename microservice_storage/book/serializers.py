from book.models import Book, BookItem
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    book_item = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        source='book',
        view_name='bookitem-detail',
    )
    """
    Serializer for Book model.
    """
    class Meta:
        model = Book
        fields = ['title', 'left_in_stock', 'book_item']


class BookItemSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        source='book_id',
        view_name='book-detail',
    )
    """
    Serializer for BookItem model.
    """
    class Meta:
        model = BookItem
        fields = ['isbn', 'status', 'book']
