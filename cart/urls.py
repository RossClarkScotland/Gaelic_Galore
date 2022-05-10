from django.urls import path
from .views import CartView
from . import views

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<item_id>', views.add_cart_item, name='add_cart_item'),
    path('adjust_cart/<item_id>', views.adjust_cart_item_qty, name='adjust_cart'),
    path('remove_cart_item/<item_id>', views.remove_cart_item, name='remove_cart_item'),
]