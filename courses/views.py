from django.views.generic import ListView, DetailView
from .models import Location, Course

# Create your views here.
class LocationListView(ListView):
    model = Location
    template_name = 'locations/location_list.html'

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

