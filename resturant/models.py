from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resturant(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(default='default.jpg', upload_to='rest_imgs')
	address = models.TextField()
	opened = models.BooleanField(default=True)
	rate = models.IntegerField(default=3)
	min_charge = models.IntegerField(default=5)
	deliver = models.IntegerField(default=30)

	def __str__(self):
		return self.name


class Item(models.Model):
	name = models.CharField(max_length=128)
	image= models.ImageField(default='default.jpg', upload_to='item_imgs')
	describtion = models.TextField()
	price = models.IntegerField(default=10)
	rate = models.IntegerField(default=2)
	available = models.BooleanField(default=True)

	resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE)
	
	def __str__(self):
		return f"from {self.resturant} to {self.user}."


class OrderItem(models.Model):
	order = models.ManyToManyField(Order)
	items = models.ManyToManyField(Item)
	quantity = models.IntegerField(default=1)
	status = models.IntegerField(default=1)