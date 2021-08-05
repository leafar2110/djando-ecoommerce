from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    fields = ('user', 'cart', 'status', 'shipping_total', 'total', 'shipping_address')
    list_display = ('__str__', 'created_at',  )


admin.site.register(Order, OrderAdmin)

# Register your models here.
