from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Announcement
from .serializers import AnnounceSeralize

class AnnounceCreate(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnounceSeralize

class AnnounceList(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnounceSeralize

class AnnounceUpdate(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnounceSeralize

class AnnounceDelete(generics.DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnounceSeralize
