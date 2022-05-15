from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import Webhook_Handler
import stripe

# logic from Stripe documentation / adapted as per Boutique Ado walkthrough project

@require_POST
@csrf_exempt
def webhook(request):
# listens for Stripe webhooks

    # set-up
    webhook_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get the webhook data and verify signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, webhook_secret
        )
    except ValueError as e:
        # invalid payload
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(status=400)

    except Exception as e:
        return HttpResponse(content=e, status=400)

    # set up a webhook handler
    handler = Webhook_Handler(request)

    # map webhook events to handler functions
    event_map = {
        'payment_.succeeded': handler.handle_payment_succeeded,
        'payment_._failed': handler.handle_payment_failed,
    }

    # get webhook type from Stripe
    event_type = event['type']

    # get handler from  event map

    event_handler = event_map.get(event_type, handler.handle_event)

    # call event handler event
    response = event_handler(event)
    return response