from django.shortcuts import render
from rest_framework import generics
from .models import Assignment
from .serializers import SubmissionSerializer
# Create your views here.


class SubmissionCreate(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionList(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = SubmissionSerializer

 


