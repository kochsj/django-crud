from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bottle
# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Bottle
    context_object_name = 'cellar'

class WineDetailView(DetailView):
    template_name = 'detail.html'
    model = Bottle

class WineCreateView(CreateView):
    template_name = 'add_bottle_form.html'
    model = Bottle
    fields = ['User', 'Winery', 'Grape', 'Year', 'Description', 'Image']

class WineUpdateView(UpdateView):
    pass

class WineDeleteView(DeleteView):
    template_name = 'delete_bottle.html'
    model = Bottle
    success_url = reverse_lazy('home')