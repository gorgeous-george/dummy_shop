from django.shortcuts import render
from django.views.generic import DetailView, ListView
from order.models import Order, OrderItem


class OrderListView(ListView):
    """
    Generic class-based view for a list of all books added to shopping cart.
    """
    model = Order
    paginate_by = 5

    def get_queryset(self):
        """
        Return list of Order objects having "status = 'Cart'"
        """
        queryset = Order.objects.filter(status='CART')
        return queryset


class OrderDetailView(DetailView):
    model = OrderItem
