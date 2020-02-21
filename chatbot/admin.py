from django.contrib import admin
from .models import Toppings, Size, Order, Response

# Register your models here.
admin.site.register(Toppings)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(Response)
