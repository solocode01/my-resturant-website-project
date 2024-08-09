from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('cart/', view_cart, name='cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('update_to_cart/', update_cart, name='update_to_cart'),
    path('reduce_cart/', reduce_cart, name='reduce_cart'),
    path('veriy_payment/<str:ref>/', veriy_payment, name='veriy_payment'),
    path('remove_cart/<int:id>', remove_cart, name='remove_cart'),
    path('checkout/', checkout, name='checkout'),
    path('menu-details/<slug:slug>/', menu_details, name='menu_details'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('success/', success, name='success'),
]

