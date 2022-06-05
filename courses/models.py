from django.db import models
from django.urls import reverse
from locations.models import Location

class Course(models.Model):
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    course_description = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    # establishes canonical url for the Course model
        return reverse('course_detail', args=[str(self.id)])