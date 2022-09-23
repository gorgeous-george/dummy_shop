from django import forms

from order.models import Order


class OrderUpdateForm (forms.ModelForm):

    class Meta:
        model = Order
        fields = ['delivery_address']
        exclude = ['id', 'client', 'status']


