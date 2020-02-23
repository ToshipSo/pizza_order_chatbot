from django.contrib import admin
from .models import Size, Order, Response, Pizza


class SizeAdmin(admin.ModelAdmin):
    list_display = ['size', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'status', 'name', 'address']
    list_editable = ['status']


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['response', 'context']


admin.site.register(Size, SizeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Pizza)
