from django.shortcuts import render
from rest_framework import generics
from .models import Enrollment
from .serializers import EnrollmentSerializer
# Create your views here.
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer