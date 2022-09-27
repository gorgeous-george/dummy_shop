from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import OrderViewSet, OrderItemViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'order', OrderViewSet, basename="order")
router.register(r'orderitems', OrderItemViewSet, basename="orderitem")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

