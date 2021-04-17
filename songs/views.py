from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Song
from .serializers import SongSerializer


# Create your views here.

class SongListView(ListView):
    model = Song
    template_name = "song_list.html"

class SongDetailView(DetailView):
    model = Song
    template_name = "song_detail.html"

class SongCreateView(LoginRequiredMixin, CreateView):
    model = Song
    template_name = "song_new.html"
    fields = ['title','project']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

## API VIEWSETS
class SongViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = (AllowAny,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer