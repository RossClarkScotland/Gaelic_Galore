from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from courses.models import Course
from profiles.models import UserProfile
import json
import time

# Logic as shown in Boutique Ado walkthrough project

class Webhook_Handler:
# handles Stripe webhooks

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
    # sends confirmation emails
        cust_email = order.email
        subject = render_to_string(
            'checkout/emails/subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/emails/body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )       

    def handle_event(self, event):
    # handles an unknown/unexpected webhook event
        return HttpResponse(
            content=f'Received unhandled webhook: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
    # handle Stripe's payment_intent.succeeded webhook
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details

        # updates profile info if save_info checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone__iexact=billing_details.phone,
                profile.default_address__iexact=billing_details.address,
                profile.default_postcode__iexact=shipping_details.address.postcode,
                profile.default_town_or_city__iexact=billing_details.address.city,
                profile.default_county__iexact=billing_details.address.county,
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try: 
                order = Order.objects.get(
                    full_name__iexact=billing_details.full_name,
                    email__iexact=billing_details.email,
                    phone__iexact=billing_details.phone,
                    address__iexact=billing_details.address,
                    postcode__iexact=shipping_details.address.postcode,
                    town_or_city__iexact=billing_details.address.city,
                    county__iexact=billing_details.address.county,
                    country__iexact=billing_details.address.country,
                    original_cart=cart,
                    stripe_pid=pid,
                    )
                
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            from django.conf import settings
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.full_name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone=billing_details.phone,
                    address=billing_details.address,
                    postcode=shipping_details.address.postcode,
                    town_or_city=billing_details.address.city,
                    county=billing_details.address.county,
                    country__iexact=billing_details.address.country,
                    original_cart=cart,
                    stripe_pid=pid,
                    )
                for item_id, item_data in json.loads(cart).items():
                    course = Course.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            course=course,
                            qty=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        from django.conf import settings
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Order created in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
    # handle Stripe's payment_intent.succeeded webhook  

        return HttpResponse(
            content=f'Recived webhook: {event["type"]}',
            status=200)