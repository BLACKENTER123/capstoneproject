from django.contrib import admin
from .models import Bookings, Menu, OrderItem, Orders, Cart
# Register your models here.
admin.site.register(Bookings)
admin.site.register(Menu)
admin.site.register(OrderItem)
admin.site.register(Orders)
admin.site.register(Cart)