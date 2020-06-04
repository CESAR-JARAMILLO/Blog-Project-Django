from django.shortcuts import render

# Django's built in Class Generic Views import
from django.views.generic import ListView
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
