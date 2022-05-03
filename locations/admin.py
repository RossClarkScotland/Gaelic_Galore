from django.contrib import admin
from .models import Location
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "description_place", "description_accomodation")

admin.site.register(Location)