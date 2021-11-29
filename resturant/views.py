from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Resturant, Item, Order
from user1.models import Cart, CartItem
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
	resturant = Resturant.objects.all()
	context = {
		'resturant':resturant
	}
	return render(request,'resturant/home.html',context)

def about(request):
	return render(request,'resturant/about.html')


def menu(request):
	context = {
		'items': menu_item.objects.all
	}
	return render(request, 'resturant/menu.html',context)


class ResturantListView(ListView):
	model = Resturant
	template_name = 'resturant/home.html'
	context_object_name = 'resturant'

	paginate_by = 2





def ResturantDetail(request, resturant_id):
	#resturant_details = Resturant.objects.filter(id=resturant_id)
	resturant_details = get_object_or_404(Resturant, id=resturant_id)
	items = resturant_details.item_set.all()
	user = request.user
	cart_items = user.cart.cartitem_set.values_list('item',flat=True)
	cart_items = list(cart_items)
	context = {
		'resturant':resturant_details,
		'items':items,
		'cart_items':cart_items,
	}
	return render(request, 'resturant/resturant_detail.html', context)


def add_to_cart(request):
	if request.is_ajax and request.method == "POST":
		try:
			#data = json.load(request)
			#item = "dasdsa"
			#item = data.get("item_id")
			item_id = request.POST.get('item_id')
			item = Item.objects.get(pk=item_id)
			resturant_id = request.POST.get('resturant_id')
			resturant = Resturant.objects.get(pk=resturant_id)
			user_id = request.POST.get('user_id')
			user = User.objects.get(pk=user_id)
			cart = user.cart

			data = {
				'item':item.id,
				'resturant':resturant.id,
				'user':user.cart.id,
				'cart':cart.id,
			}
			cart_item = CartItem.objects.create(cart=cart)
			cart_item.resturant.set([resturant])
			cart_item.item.set([item])
			cart_item.quantity = 10
			cart_item.save()
			#cart_item = CartItem(cart=cart, resturant= resturant, item=item, quantity=100)
			#cart_item.save()
			return JsonResponse(data, status=200)
		except Exception as e:
			return JsonResponse({"error":str(e)}, status=404)


def remove_from_cart(request):
	if request.is_ajax and request.method == "POST":
		try:
			item_id = request.POST.get('item_id')
			item = Item.objects.get(pk=item_id)
			user_id = request.POST.get('user_id')
			user = User.objects.get(pk=user_id)
			cart = user.cart

			data = {
				'item':item.id,
				'user':user.cart.id,
				'cart':cart.id,
			}

			item = user.cart.cartitem_set.filter(item=item).first()
			item.delete()

			return JsonResponse(data, status=200)

		except Exception as e:
			return JsonResponse({"error":str(e)}, status=404)


class OrderListView(ListView):
	model = Order
	template_name = 'resturant/order.html'
	context_object_name = 'orders'

	def get_queryset(self):
		user = self.request.user
		return Order.objects.filter(user=user)


#class OrderDetailView(DetailView):
#	model = Order
#	template_name = 'resturant/order_detail.html'
#	context_object_name = 'order'
#
#	def get_queryset(self):
#		order = Order.objects.filter(pk=self.kwargs.get('pk'))
#		return order

	
def OrderDetail(request,order_id):
	order = Order.objects.filter(pk=order_id).first()
	items = order.items.all()

	context = {
		'items':items,
	}

	return render(request,'resturant/order_detail.html', context)


