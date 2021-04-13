from django import urls
from django.urls import path

from .views import RecordingListView, RecordingDetailView, RecordingCreateView

urlpatterns = [
    path('new/', RecordingCreateView.as_view(), name='recording_new'),
    path('<int:pk>/', RecordingDetailView.as_view(), name='recording_detail'),
    path('', RecordingListView.as_view(), name='recording_list')
]