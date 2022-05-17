from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ProfileView(TemplateView):
# renders the index/home page
    template_name = 'profile.html'


"""
def profile(request):
# Display the user's profile

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
"""