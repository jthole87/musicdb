from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recording


# Create your views here.

class RecordingListView(ListView):
    model = Recording
    template_name = "recording_list.html"

class RecordingDetailView(DetailView):
    model = Recording
    template_name = "recording_detail.html"

class RecordingCreateView(LoginRequiredMixin, CreateView):
    model = Recording
    template_name = "recording_new.html"
    fields = ['name','notes','recording','song']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)