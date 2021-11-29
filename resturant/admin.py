from django.contrib import admin
from .models import Item, Order, Resturant, OrderItem
# Register your models here.

#class ItemAdmin(admin.ModelAdmin):
#	filter_horizontal = ("Resturants",)

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Resturant)