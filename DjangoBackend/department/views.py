from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .models import Department
from .serializers import DepartmentSerializer
# Create your views here.

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
