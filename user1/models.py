from django.db import models
from django import forms
from django.contrib.auth.models import User
from resturant.models import Resturant, Item
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	address = models.TextField()
	phone = models.CharField(max_length=11)

	def __str__(self):
		return self.user.username


class Cart(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"Cart of {self.user.username} "

class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	resturant = models.ManyToManyField(Resturant)
	item = models.ManyToManyField(Item)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.item}"




	
