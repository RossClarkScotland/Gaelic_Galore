from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

# logic learned from Boutique Ado walkthrough project


@login_required()
def profile(request):
    """ displays user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sgoinneil! Profile updated!')
        else:
            messages.error(request, '>Tha sinn duilich. Update failed.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ shows previous orders"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This shows your past order: {order_number}. '
        'We sent you a wee confirmation email on the day.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
