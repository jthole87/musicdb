from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = (IsAdminUser, IsAuthenticatedOrReadOnly)
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = CustomUserSerializer