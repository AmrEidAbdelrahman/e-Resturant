from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Resturant, Item, Order, OrderItem
from user1.models import Cart, CartItem
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	resturant = Resturant.objects.all()
	context = {
		'resturant':resturant
	}
	return render(request,'resturant/home.html',context)

def about(request):
	return render(request,'resturant/about.html')

@login_required(login_url='/login/')
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




@login_required(login_url='/login/')
def ResturantDetail(request, resturant_id):
	#resturant_details = Resturant.objects.filter(id=resturant_id)
	resturant_details = get_object_or_404(Resturant, id=resturant_id)
	items = resturant_details.item_set.all()
	user = request.user

	if user.cart_set.last():
		cart = user.cart_set.last()
	else:
		cart = Cart.objects.create(user=user)
		#cart.user = user


	cart_items = cart.cartitem_set.values_list('item',flat=True)
	cart_items = list(cart_items)
	context = {
		'resturant':resturant_details,
		'items':items,
		'cart_items':cart_items,
	}
	return render(request, 'resturant/resturant_detail.html', context)

@login_required(login_url='/login/')
def add_to_cart(request):
	if request.is_ajax and request.method == "POST":
		try:
			item_id = request.POST.get('item_id')
			item = Item.objects.get(pk=item_id)
			resturant_id1 = request.POST.get('resturant_id')
			resturant = Resturant.objects.get(pk=resturant_id1)
			user_id = request.POST.get('user_id')
			user = User.objects.get(pk=user_id)
			cart = user.cart_set.last()

			try:
				resturant_id2 = cart.cartitem_set.first().item.resturant.id
				if int(resturant_id1) == int(resturant_id2):
					print("#############++##########")
					#pass	
				else:
					print("############----##########")
					cart.cartitem_set.all().delete()
			except:
				d = 1


			data = {
				'item':item.id,
				'resturant':resturant.id,
				'user':user.id,
				'cart':cart.id,
			}

			cart_item = CartItem(cart=cart, item=item)
			cart_item.save()
			return JsonResponse(data, status=200)
		except Exception as e:
			return JsonResponse({"error":str(e)}, status=404)

@login_required(login_url='/login/')
def remove_from_cart(request):
	if request.is_ajax and request.method == "POST":
		try:
			item_id = request.POST.get('item_id')
			item = Item.objects.get(pk=item_id)
			user_id = request.POST.get('user_id')
			user = User.objects.get(pk=user_id)
			cart = user.cart_set.last()

			data = {
				'item':item.id,
				'user':cart.id,
				'cart':cart.id,
			}

			item = cart.cartitem_set.filter(item=item).last()
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

@login_required(login_url='/login/')	
def OrderDetail(request,order_id):

	order = Order.objects.filter(pk=order_id).first()
	items = order.orderitem_set.all()

	context = {
		'items':items,
	}

	return render(request,'resturant/order_detail.html', context)

@login_required(login_url='/login/')
def OrderNow(request):
	if request.method == "POST":
		user_id = request.POST.get('user_id')
		user = User.objects.get(pk=user_id)
		cart = user.cart_set.all().last()
		resturant = cart.cartitem_set.first().item.resturant
		item_quantity = cart.cartitem_set.all()
		
		order = Order.objects.create(user=user,resturant=resturant)
		print("#################")
		print(item_quantity)
		for i in item_quantity:
			order_item = OrderItem(order=order, items=i.item, quantity=i.quantity)
			#order_item.order.set([order])
			#order_item.items.set([i])
			#order_item.quantity = q
			#oreder_item = order.orderitem_set.add()
			#order_item.item = i
			#order_item.quantity = q
			order_item.save()
		order.save()
		cart.cartitem_set.all().delete()
		'''
		context = {
			#'user_':user_id,
			#'quantity':dict(quantity),
			#'order_item':order_item,
			'resturant':resturant
		}
		'''
	#return render(request, 'resturant/order_now.html', context)
	return HttpResponseRedirect(reverse('order'))

