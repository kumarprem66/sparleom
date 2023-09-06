from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Category
from .serializers import CategorySerializer

class CategoryCrud(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer