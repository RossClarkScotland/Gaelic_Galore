from django.db import models
from django.urls import reverse

class Location(models.Model):
    name = models.CharField(max_length=100)
    description_place = models.TextField()
    description_accomodation = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
    # establishes canonical url for the Location model
        return reverse('location_detail', args=[str(self.id)])
