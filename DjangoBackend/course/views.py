from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics,viewsets
# Create your views here.
from .models import Course
from .serializers import CourseSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseListUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseListDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()

   
class getSingleCourse(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



def getInstructorsCourse(request,instruc_id):
    try:
        courses = Course.objects.filter(Instructor=instruc_id)
        
        data = [{'id':course.id, 'course_name': course.course_name, 'duration': course.duration, 'rating': course.rating,'is_available':course.is_available,'description':course.description,'course_price':course.course_price,'rating_count':course.rating_count,"course_language":course.course_language,"student_enrolled":course.student_enrolled} for course in courses]
        return JsonResponse(data, safe=False)
        
    except Exception as e:
        return JsonResponse({'error':str(e)})
    

def courseByCategory(request,cat_id):
   
    try:
        courses = Course.objects.filter(course_category=cat_id)
        data = [{'id':course.id, 'course_name': course.course_name, 'duration': course.duration, 'rating': course.rating,'is_available':course.is_available,'description':course.description,'course_price':course.course_price,'rating_count':course.rating_count,"course_category":course.course_language,"student_enrolled":course.student_enrolled} for course in courses]
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error':e})