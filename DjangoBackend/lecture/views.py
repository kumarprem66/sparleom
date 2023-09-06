from django.shortcuts import render
from .models import Lecture
from .serializers import LectureSerializer
from rest_framework import generics,viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from instructor.models import Instructor
from course.models import Course
# Create your views here.

class createLecture(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class ListLecture(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class updateLecture(generics.UpdateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class deleteLecture(generics.DestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class getSingleLecture(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    

def getLecturesOfCourse(request,course_id):
    try:
        lectures = Lecture.objects.filter(lecture_course_name_id=course_id)
        
        data = [{'id':lecture.id, 'topic_title': lecture.topic_title, 'timing': lecture.timing, 'meeting_url': lecture.meeting_url} for lecture in lectures]
        return JsonResponse(data, safe=False)
        
    except Exception as e:

        return JsonResponse({'error':str(e)})
    

class InstructorLectures(APIView):
    def get(self,request,instructor_id):
        try:
            courses = Course.objects.filter(Instructor=instructor_id)

            lectures = Lecture.objects.filter(lecture_course_name__in=courses)

            serializer = LectureSerializer(lectures,many=True)

            return Response(serializer.data,status=status.HTTP_200_OK)
    
        except Course.DoesNotExist:
            return Response(
                {"message": "Instructor or associated courses not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Lecture.DoesNotExist:
            return Response(
                {"message": "Lectures not found for this instructor."},
                status=status.HTTP_404_NOT_FOUND
            )
