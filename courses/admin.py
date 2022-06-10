from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    """course fields to display in admin"""
    list_display = ("title", "level", "date", "price")

# Register your models here.


admin.site.register(Course)
