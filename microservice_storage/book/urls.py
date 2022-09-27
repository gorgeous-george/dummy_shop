from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book.views import BookViewSet, BookItemViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename="book")
router.register(r'bookitems', BookItemViewSet, basename="bookitem")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

