from django.shortcuts import render
# Django's built in Class Generic Views import
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/index.html'
    # Designates the name of the variable to use in the context.
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 3

class EntryView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title', 'entry_text']

    # Overrides form valid method
    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)
