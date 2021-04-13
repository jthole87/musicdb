from django import urls
from django.urls import path

from .views import ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name='project_new'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('', ProjectListView.as_view(), name='project_list')
]