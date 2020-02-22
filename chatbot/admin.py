from django.contrib import admin
from .models import Toppings, Size, Order, Response


# Register your models here.
class ToppingsAdmin(admin.ModelAdmin):
    list_display = ['topping', 'price']


class SizeAdmin(admin.ModelAdmin):
    list_display = ['size', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'status', 'name', 'address']
    list_editable = ['status']


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['response', 'context']


admin.site.register(Toppings, ToppingsAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Response, ResponseAdmin)
