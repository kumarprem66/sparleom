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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


class InstructorLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            # Check if an instructor with the provided email and password exists
            instructor = Instructor.objects.get(email=email, password=password)
            return Response({'message': 'Instructor exists.'}, status=status.HTTP_200_OK)
        except Instructor.DoesNotExist:
            return Response({'error': 'Instructor not found or invalid credentials.'}, status=status.HTTP_404_NOT_FOUND)