from django.http import HttpResponse

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

    def handle_payment_succeeded(self, event):
    # handle Stripe's payment_intent.succeeded webhook
    
        return HttpResponse(
            content=f'Received webhook: {event["type"]}',
            status=200)

    def handle_payment_failed(self, event):
    # handle Stripe's payment_intent.succeeded webhook  

        return HttpResponse(
            content=f'Recived webhook: {event["type"]}',
            status=200)