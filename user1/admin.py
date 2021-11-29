from django.contrib import admin
from .models import Profile, Cart, CartItem
from django.contrib.auth.models import User
# Register your models here.

#class CartItemAdmin(admin.StackedInline):
#	model = User.cart.through
#	extra = 1

#class CartAdmin(admin.ModelAdmin):
#	inline = [CartItemAdmin]

class CartItemAdmin(admin.ModelAdmin):
	filter_horizontal = ("item",)

admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)