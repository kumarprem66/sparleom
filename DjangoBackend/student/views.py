from django.shortcuts import render
from rest_framework import generics
from .models import Student
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serialize import StudentSerializer
# Create your views here.

from rest_framework import viewsets
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Student
from course.models import Course  # Replace with the actual import for your Course model

# class AddCourseToStudent(APIView):
#     def post(self, request, pk):
#         try:
#             student = get_object_or_404(Student, pk=pk)
#             course_id = request.data.get('course_id')
            
#             # Check if the course with the given ID exists
#             course = get_object_or_404(Course, pk=course_id)
            
#             # Add the course to the student's course_ids list
#             student.course_ids.add(course)
            
#             # Save the student object
#             student.save()
            
#             return Response({'message': 'Course added to student successfully.'}, status=status.HTTP_200_OK)
#         except Student.DoesNotExist:
#             return Response({'error': 'Student not found.'}, status=status.HTTP_404_NOT_FOUND)
#         except Course.DoesNotExist:
#             return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddCourseToStudent(APIView):
    def post(self, request, pk):
        try:
            student = get_object_or_404(Student, pk=pk)
            course_id = request.data.get('course_id')
            
            # Check if the course with the given ID exists
            course = get_object_or_404(Course, pk=course_id)
            
            # Check if the student already has the course
            if course in student.course_ids.all():
                return Response({'error': 'You have already purchased this course.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Add the course to the student's course_ids list
            student.course_ids.add(course)
            
            # Save the student object
            student.save()
            
            return Response({'message': 'Course added to student successfully.'}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
