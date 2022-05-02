from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Location(models.Model):
    name = models.CharField(max_length=100)
    description_place = models.TextField(unique=True)
    description_accomodation = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    # establishes canonical url for the Course model
        return reverse('course_detail', args=[str(self.id)])