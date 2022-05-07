from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class CartView(TemplateView):
# renders the shopping cart page
    template_name = 'cart/cart.html'



def add_cart_item(request, course_id):
# adds item to cart
# logic pattern learned from Boutique Ado walktrhrough project
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if course_id in list(cart.keys()):
        cart[course_id] += qty
    else:
        cart[course_id] = qty

    request.session['cart'] = cart
    return redirect(redirect_url)