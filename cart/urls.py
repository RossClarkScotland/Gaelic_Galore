from django.urls import path
from .views import CartView
from . import views

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<course_id>', views.add_cart_item, name='add_cart_item'),
]