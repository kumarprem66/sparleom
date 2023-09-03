from django.shortcuts import render
from .models import Lecture
from .serializers import LectureSerializer
from rest_framework import generics,viewsets
from django.http import JsonResponse
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