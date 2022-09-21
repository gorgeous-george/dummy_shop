from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from order.models import Order, OrderItem


class OrderView(View):
    """
    Generic class-based view for a list of all books added to shopping cart.
    """
    model = Order
    paginate_by = 5

    def get_queryset(self):
        """
        Return list of Order objects having "status = 'Cart'"
        """
        queryset = Order.objects.filter(status='CART').select_related("client")
        return queryset


class OrderItemListView(ListView):
    """
    Generic class-based view for a list of all books added to shopping cart.
    """
    model = OrderItem
    paginate_by = 5

    def get_queryset(self):
        """
        adding related information on book and order details
        """
        queryset = OrderItem.objects.select_related("book_id", "order_id")
        return queryset

    def get_context_data(self, **kwargs):
        """
        adding related information on user/client
        """
        client = Order.objects.select_related("client").get(id=1)  # todo: order.id = orderitem.order.id
        context = super().get_context_data(**kwargs)
        context["client"] = client
        return context
