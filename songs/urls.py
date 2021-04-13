from django import urls
from django.urls import path

from .views import SongListView, SongDetailView, SongCreateView

urlpatterns = [
    path('new/', SongCreateView.as_view(), name='song_new'),
    path('<int:pk>/', SongDetailView.as_view(), name='song_detail'),
    path('', SongListView.as_view(), name='song_list')
]