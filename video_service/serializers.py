from rest_framework import serializers
from .models import Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id', 'title', 'video_id', 'description', 'publish_date', 'thumbnail_meta', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Videos.objects.create(**validated_data)