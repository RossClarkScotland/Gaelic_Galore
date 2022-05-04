from django.views.generic import ListView, DetailView
from .models import Location

# Create your views here.
class LocationListView(ListView):
# returns all locations
    model = Location
    context_object_name = 'location_list'
    template_name = 'locations/location_list.html'

class LocationDetailView(DetailView):
# returns individual locations
    model = Location
    context_object_name = 'location'
    template_name = 'locations/location_detail.html'