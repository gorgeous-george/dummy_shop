from django.contrib.auth import get_user_model
from django.db import models

"""
Currently active user model is imported for representing clients. 
This method will return default django User model or the custom user model if one would be specified.
"""
User = get_user_model()


class Book(models.Model):
    """
    Model representing a Book as marketing object showed to users via web-front layer.
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    cover = models.ImageField(upload_to='book/')
    left_in_stock = models.IntegerField(default=0)       #  todo: to make it calculated based on book instances left in stock (API storage)
    storage_book_id = models.IntegerField(default=0)     #  todo: to make it synchronized with storage's Book.id

    class Meta:
        ordering = ["author", "genre", "title", "left_in_stock"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
