from order.models import Order, OrderItem
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        source='order',
        view_name='orderitem-detail',
    )
    """
    Serializer for Order model.
    """
    class Meta:
        model = Order
        fields = ['client_email', 'status', 'delivery_address', 'shop_order_id', 'order_item']


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        source='book_id',
        view_name='book-detail',
    )
    order = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        source='order_id',
        view_name='order-detail',
    )
    """
    Serializer for OrderItem model.
    """
    class Meta:
        model = OrderItem
        fields = ['book_item', 'quantity', 'order', 'book']
