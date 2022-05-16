import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from courses.models import Course


# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=20, null=False, editable=False)
    full_name = models.CharField(max_length=60, null=False, blank=False, default='John Doe')
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _create_order_number(self):
    # generates unique order number via UUID
        return uuid.uuid4().hex.upper()

    def update_total(self):
    # update total any time a line item is added
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
    # sets order number if not already set
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    course = models.ForeignKey(Course(), null=False, blank=False, on_delete=models.CASCADE)
    qty = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
    # sets lineitem total and updates order total

        self.lineitem_total = self.course.price * self.qty
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.course.sku} on order {self.order.order_number}'