from django.urls import path

from order.views import OrderListView, OrderDetailView

urlpatterns = [
    path('cart/', OrderListView.as_view(), name='shop_cart'),                    # shopping cart page
    path('order_confirmation/', OrderDetailView.as_view(), name='shop_order'),    # order page
    ]