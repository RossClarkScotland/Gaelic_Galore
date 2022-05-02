from django.contrib import admin
from .models import Location, Course

class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "description_place", "description_accomodation")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "date", "price")

# Register your models here.
admin.site.register(Location)
admin.site.register(Course)