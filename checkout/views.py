from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from courses.models import Course
from cart.contexts import cart_contents
import stripe

# Logic structure learned from Boutique Ado walkthrough project

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address': request.POST['address'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    course = Course.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            course=course,
                            qty=item_data,
                        )
                        order_line_item.save()

                except Course.DoesNotExist:
                    messages.error(request, (
                        "Tha sinn duilich! We can't find that course."
                        )
                    )
                    order.delete()
                    return redirect(reverse('cart'))
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'Tha sinn duilich! There was a problem with your form. \
                Please review your details.')
    
    else:
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, "Mo chreach! Your bag is empty.")
            return redirect(reverse('course_list'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'No Stripe public key found. \
            Did you set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
   # handles successful payments

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Sgonneil! Your order was successful! \
        Order number is {order_number}. You will receive confirmation \
        of your order at {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)