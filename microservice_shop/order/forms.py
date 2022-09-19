from django import forms


class OrderForm(forms.Form):
    email = forms.EmailField(required=True)
    delivery_address = forms.CharField(required=True)
    additional_details = forms.CharField(widget=forms.Textarea, required=True)
