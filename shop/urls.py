from django.urls import path
from .views import *

urlpatterns=[
    path('', product_list, name='product_list'),
    path('cart/', cart, name='cart'),
    path('delete_cart_item/<int:pk>', delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', edit_cart_item, name='edit_cart_item'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    
    path('orders/', orders, name='orders'),
    path('cart/create_order', create_order, name='create_order'),
    
]


