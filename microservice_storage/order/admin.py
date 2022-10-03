from django.contrib import admin
from order.models import Order, OrderItem

@admin.action(description='Complete order')
def make_completed(modeladmin, request, queryset):
    queryset.update(status='SUCCESS')

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
    list_display = ["client_email", "status", "delivery_address", "shop_order_id"]
    list_filter = ["id", "client_email", "status"]
    ordering = ("id", "client_email", "status")
    actions = [make_completed]


