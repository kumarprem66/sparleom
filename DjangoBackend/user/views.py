from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerialiser
# Create your views here.


class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
