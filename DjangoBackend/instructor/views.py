from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from .models import Instructor
from .selializers import InstructorSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class InstructorListAPIView(ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorCreateAPIView(CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    # def perform_create(self, serializer):
    #     validated_data = serializer.validated_data
    #     password = validated_data.pop('password')
    #     instructor = serializer.save()
    #     instructor.set_password(password)
    #     instructor.save()
    

class InstructorUpdateAPIView(UpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDeleteAPIView(DestroyAPIView):
    queryset = Instructor.objects.all()
   
