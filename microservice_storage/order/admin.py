from django.contrib import admin
from order.models import Order, OrderItem


class OrderInline(admin.TabularInline):
    """
    Inline Model representing Order Items included to the Order
    """
    model = OrderItem
    extra = 1

    def get_queryset(self, request):
        """
        function for returning the Model queryset
        """
        obj = OrderItem.objects.filter(book_item__status="AVAILABLE")
        return obj


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin Model representing an Order created by user via web-front layer.
    """
    inlines = [OrderInline, ]
    list_display = ["client_email", "status", "delivery_address", "shop_order_id"]
    list_filter = ["id", "client_email", "status"]
    ordering = ("id", "client_email", "status")

    def get_queryset(self, request):
        """
        function for returning the Model queryset
        """
        return super(OrderAdmin, self).get_queryset(request)
