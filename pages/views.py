from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
# renders the index/home page
    template_name = 'index.html'

class ContactPageView(TemplateView):
# renders the index/home page
    template_name = 'contact.html'