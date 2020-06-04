from django.shortcuts import render

# Django's built in Class Generic Views import
from django.views.generic import ListView, DetailView
from .models import Entry

class HomeView(ListView):
    model = Entry
    template_name = 'entries/index.html'
    # Designates the name of the variable to use in the context.
    context_object_name = 'blog_entries'

class EntryView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'
