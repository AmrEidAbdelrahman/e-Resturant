from django.contrib import admin
from django.urls import path
from . import views as resturant_views

urlpatterns = [
    path('', resturant_views.ResturantListView.as_view(), name='menu-home'),
    path('add-to-cart/', resturant_views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/', resturant_views.remove_from_cart, name='remove-from-cart'),
    
    path('resturant/<int:resturant_id>/', resturant_views.ResturantDetail, name='resturant-detail'),
    
    path('about/', resturant_views.about, name='about'),
]
