from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_location(request):
    # adds location to the site
    if not request.user.is_superuser:
        messages.error(request, 'Tha sinn duilich. This page is only for site admin.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save()
            messages.success(request, 'Sgonneil! New location added!')
            return redirect(reverse('location_detail', args=[location.id]))
        else:
            messages.error(request, 'Tha sinn duilich! Failed to add location.')
    else:
        form = LocationForm()

    template = 'locations/add_location.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_location(request, location_id):
    # edits a location on the site
    if not request.user.is_superuser:
        messages.error(request, 'Tha sinn duilich. This page is only for site admin.')
        return redirect(reverse('home'))
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


@login_required
def delete_location(request, location_id):
    """ delete location """
    if not request.user.is_superuser:
        messages.error(request, 'Tha sinn duilich. This page is only for site admin.')
        return redirect(reverse('home'))
    location = get_object_or_404(Location, pk=location_id)
    location.delete()
    messages.success(request, 'Sgonneil! Location deleted!')
    return redirect(reverse('location_list'))
