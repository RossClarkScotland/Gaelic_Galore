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


def edit_location(request, location_id):
# edits a location on the site
    location = get_object_or_404(Location, pk=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sgonneil! Updated location!')
            return redirect(reverse('location_detail', args=[location.id]))
        else:
            messages.error(request, 'Tha sin duilich. Failed to update location.')
    else:
        form = LocationForm(instance=location)
        messages.info(request, f'You are editing {location.name}')

    template = 'locations/edit_location.html'
    context = {
        'form': form,
        'location': location,
    }

    return render(request, template, context)