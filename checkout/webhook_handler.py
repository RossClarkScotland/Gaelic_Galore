from django.http import HttpResponse
from .models import Order, OrderLineItem
from courses.models import Course
import json
import time

# Logic as shown in Boutique Ado walkthrough project

class Webhook_Handler:
# handles Stripe webhooks

    def __init__(self, request):
        self.request = request

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

        order_exists = False
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
                )
            
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        except Order.DoesNotExist:
            try:
                for item_id, item_data in json.loads(cart).items():
                    order = Order.objects.create(
                        full_name=billing_details.full_name,
                        email=billing_details.email,
                        phone=billing_details.phone,
                        address=billing_details.address,
                        postcode=shipping_details.address.postcode,
                        town_or_city=billing_details.address.city,
                        county=billing_details.address.county,
                        country__iexact=billing_details.address.country,
                    )
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

    def handle_payment_intent_payment_failed(self, event):
    # handle Stripe's payment_intent.succeeded webhook  

        return HttpResponse(
            content=f'Recived webhook: {event["type"]}',
            status=200)