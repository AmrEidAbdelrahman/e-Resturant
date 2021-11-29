from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Profile, Cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from resturant.models import Item

from django.db.models import Count, Sum
# Create your views here.




def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"You successfuly signed up, sign in with {username} Now!")
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request, 'user1/register.html',{'form':form})


@login_required
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'You Profile save')
			return redirect('profile')
	else:
		p_form = ProfileUpdateForm(instance=request.user.profile)
		u_form = UserUpdateForm(instance=request.user)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'user1/profile.html', context)


@login_required
def CartList(request):
	user = get_object_or_404(User, id=request.user.id)
	it = user.cart.cartitem_set.values_list('item')
	items = Item.objects.filter(pk__in= it)
	num_of_items = items.aggregate(Count('id'))
	price = items.aggregate(Sum('price'))

	page = request.GET.get('page')
	
	paginator = Paginator(items, 2)
	
	
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)

	context = {
		'items':items,
		'num_of_items':num_of_items,
		'price':price,
	}

	return render(request, 'user1/cart.html', context)


