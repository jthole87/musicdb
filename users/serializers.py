from rest_framework import serializers

from .models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = (['projects','first_name','last_name'])