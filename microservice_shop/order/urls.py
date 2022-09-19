from django.urls import path


urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='shop_cart'),                    # shopping cart page
    path('order_confirmation/', OrderDetailView.as_view(), name='shop_order'),    # order page
    ]