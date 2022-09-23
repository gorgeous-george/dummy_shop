from django.urls import path

from order.views import OrderDetailView, CartCreate, OrderConfirm

urlpatterns = [
    path('cart/<int:pk>', OrderDetailView.as_view(), name='shop_cart'),      # shopping cart page
    path('cart_create/<int:pk>', CartCreate.as_view(), name='cart_create'),    # adding a book to shopping cart
    path('confirm/<int:pk>', OrderConfirm.as_view(), name='order_confirm'),    # order confirmation
    ]