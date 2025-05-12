from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('products', views.products, name='products'),
    path('product', views.product, name='product'),
    path('sell_phone', views.sell_phone, name='sell_phone'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
]