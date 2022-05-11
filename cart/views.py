from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from courses.models import Course

# Create your views here.
class CartView(TemplateView):
# renders the shopping cart page
    template_name = 'cart/cart.html'



def add_cart_item(request, item_id):
# adds item to cart
# logic pattern learned from Boutique Ado walktrhrough project
    course = get_object_or_404(Course, pk=item_id)
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += qty
        messages.success(request, f'Number of {course.title} participants updated!')
    else:
        cart[item_id] = qty
        messages.success(request, f'{course.title} added to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

 

def adjust_cart_item_qty(request, item_id):
# changes number of items in the cart
# logic pattern learned from Boutique Ado walktrhrough project
    course = get_object_or_404(Course, pk=item_id)
    qty = int(request.POST.get('qty'))
    cart = request.session.get('cart', {})

    if qty > 0:
        cart[item_id] = qty
        messages.success(request, f'Number of {course.title} participants updated!')
    else:
        cart.pop(item_id)
        messages.success(request, f'{course.title} removed from your cart')

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_cart_item(request, item_id):
# removes items from the cart
# logic pattern learned from Boutique Ado walktrhrough project

    try:
        course = get_object_or_404(Course, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)