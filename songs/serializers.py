from rest_framework import serializers

from.models import Song

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = (['author','title','created_on',
                            'last_updated','project'])