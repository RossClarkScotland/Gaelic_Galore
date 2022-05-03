from django.views.generic import ListView, DetailView
from .models import Location

# Create your views here.
class LocationListView(ListView):
    model = Location
    context_object_name = 'location_list'
    template_name = 'locations/location_list.html'

class LocationDetailView(DetailView):
    model = Location
    context_object_name = 'location'
    template_name = 'locations/location_detail.html'