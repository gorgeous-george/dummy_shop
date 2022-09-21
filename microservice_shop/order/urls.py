from django.urls import path

from order.views import OrderView, OrderItemListView

urlpatterns = [
    path('cart/', OrderItemListView.as_view(), name='shop_cart'),                    # shopping cart page
    path('order_confirmation/', OrderView.as_view(), name='shop_order'),    # order page
    ]