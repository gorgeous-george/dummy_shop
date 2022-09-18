from django.contrib import admin
from order.models import Order, OrderItem


class OrderInline(admin.TabularInline):
    """
    Inline Model representing Order Items included to the Order
    """
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin Model representing an Order created by user via web-front layer.
    """
    inlines = [OrderInline, ]
    list_display = ["client", "status", "delivery_address"]
    list_filter = ["id", "client"]
    ordering = ("id", "client")

    def get_queryset(self, request):
        """
        function for returning the Model queryset
        """
        return super(OrderAdmin, self).get_queryset(request)

