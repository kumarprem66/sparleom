from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import Instructor
from .selializers import InstructorSerializer
# from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.




class InstructorListAPIView(ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorCreateAPIView(CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorUpdateAPIView(UpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDeleteAPIView(DestroyAPIView):
    queryset = Instructor.objects.all()
   
class SingleInstructor(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
