from rest_framework import serializers

from.models import Recording

class RecordingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recording
        fields = (['author','name','created_on',
                            'notes','recording','song'])