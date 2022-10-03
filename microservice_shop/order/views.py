from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from book.models import Book
from order.forms import OrderUpdateForm
from order.models import Order, OrderItem


class OrderDetailView(LoginRequiredMixin, DetailView):
    """
    Class-based view for a list of all books added to shopping cart.
    """
    model = Order
    template_name = 'order/order_detail.html'

    def get_object(self):
        """
        Returning the user's Order having status "CART" (supposed to have only one such Order at any point of time)
        """
        obj = Order.objects.get(client=self.request.user, status='CART')
        return obj


class CartCreate(LoginRequiredMixin, CreateView):
    """
    Class-based view used for a form appeared while adding a book to shopping cart.
    """
    model = OrderItem
    fields = ['order_id', 'book_id', 'quantity']

    def get_initial(self, *args, **kwargs):
        """
        Add associated order to form template
        """
        # Call the base implementation first
        initial = super(CartCreate, self).get_initial()
        # Get the order and the book
        order, created = Order.objects.get_or_create(
            client=self.request.user,
            status='CART',
            defaults={
                'delivery_address': 'please input delivery address'
            },
        )
        # Put values to 'initial'
        initial['quantity'] = '1'
        initial['order_id'] = order
        initial['book_id'] = get_object_or_404(Book, pk=self.kwargs['pk'])
        return initial

    def form_valid(self, form):
        """
        Form validation, and automatized adding a new Order Item to the database
        """
        return super(CartCreate, self).form_valid(form)


class OrderConfirm(LoginRequiredMixin, UpdateView):
    """
    Class-based view used for the order finalization and confirmation
    """
    model = Order
    form_class = OrderUpdateForm
    template_name = 'order/order_confirm.html'

    def get_initial(self, *args, **kwargs):
        """
        Add associated order items to form template
        """
        # Call the base implementation first
        initial = super(OrderConfirm, self).get_initial()
        # Put values to 'initial'
        initial['delivery_address'] = 'please enter a delivery address'
        return initial

    def form_valid(self, form):
        """
        Form validation, and updating of Order status from "CART" to "ORDERED" in the database
        """
        result = super(OrderConfirm, self).form_valid(form)
        obj = self.get_object()
        obj.status = 'ORDERED'
        obj.save()
        return result
