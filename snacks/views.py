from django.shortcuts import render
from django.views.generic import TemplateView

# here we define html files
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'