from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# as shown in Boutique Ado walkthrough project

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
# updates order total upon lineitem update/create
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
# updates order total upon lineitem delete
    instance.order.update_total()