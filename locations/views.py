from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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
# adds location to the site
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sgonneil! New location added!')
            return redirect(reverse('add_location'))
        else:
            messages.error(request, 'Tha sinn duilich! Failed to add location.')
    else:
        form = LocationForm()
        
    template = 'locations/add_location.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



