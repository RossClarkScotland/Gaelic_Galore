from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Location
from .forms import LocationForm

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

def add_location(request):
# adds a location to the site
    form = LocationForm()
    template = 'locations/add_location.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



