from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Recording
from .serializers import RecordingSerializer

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
    fields = (['name','notes','recording','song','project'])

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

## API VIEWSETS

class RecordingViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

