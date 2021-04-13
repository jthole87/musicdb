from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project


# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = "project_list.html"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "project_new.html"
    fields = ['name']
