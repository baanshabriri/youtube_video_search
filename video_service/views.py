from django.shortcuts import render
from rest_framework import filters

# Create your views here.
from video_service.models import Videos
from video_service.serializers import VideoSerializer
from rest_framework import generics


class VideoList(generics.ListCreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer