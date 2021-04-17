from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Project
from .serializers import ProjectSerializer


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

## API VIEWSETS
class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer