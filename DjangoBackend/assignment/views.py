from django.shortcuts import render
from rest_framework import generics
from .models import Assignment
from .serializers import AssignmentSerialiser
# Create your views here.


class AsignmentCreate(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerialiser

class AsignmentList(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerialiser

class AsignmentUpdate(generics.UpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerialiser

class AsignmentDelete(generics.DestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerialiser