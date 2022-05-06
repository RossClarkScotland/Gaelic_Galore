from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CartView(TemplateView):
# renders the shopping cart page
    template_name = 'cart/cart.html'