from order.models import Order, OrderItem
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """
    class Meta:
        model = Order
        fields = ['id', 'client_email', 'status', 'delivery_address', 'shop_order_id']


class OrderItemSerializer(serializers.ModelSerializer):
    book_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    """
    Serializer for OrderItem model.
    """
    class Meta:
        model = OrderItem
        fields = ['quantity', 'book_id', 'order_id']
