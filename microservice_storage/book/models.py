import uuid

from django.contrib.auth import get_user_model
from django.db import models

"""
Currently active user model is imported for representing clients. 
This method will return default django User model or the custom user model if one would be specified.
"""
User = get_user_model()


class Book(models.Model):
    """
    Model representing a Book as real book object stored at "storage".
    There is no need to have all details such as "author, description, genre, etc."
    In this case it is just an object stored. It is enough to have at least the object's ID to manage it.
    """
    # todo: to make Book.id synchronized with shop's Book.book_id_storage
    title = models.CharField(max_length=200)
    left_in_stock = models.IntegerField(default=0)       # todo: to make it calculated based on book instances left in stock (API storage)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class BookItem(models.Model):
    """
    Model representing book items, namely book copies available at "storage"
    There are can be a number of unique copies of the same book
    """
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    isbn = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    AVAILABLE = 'AVAILABLE'
    ORDERED = 'ORDERED'
    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (ORDERED, 'Ordered'),
    ]
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=AVAILABLE)

    class Meta:
        ordering = ["book_id", "isbn", "status"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.isbn
