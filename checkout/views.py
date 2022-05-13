from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Logic as shown in Boutique Ado walkthrough project

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Mo chreach! Your bag is empty.")
        return redirect(reverse('course_list'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J2jhOBsZwD5BzE8wyRJYa4tDBYik8umWwqV6KqmNOMde6HRryTqzVChPFK9ukAVWEYqmNCvB038vABPvAS1zIAN00xbOtfXxJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)