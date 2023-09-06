from django.urls import path,include
from .views import createLecture,ListLecture,updateLecture,deleteLecture,getLecturesOfCourse,getSingleLecture,InstructorLectures
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'lectures',getSingleLecture)

urlpatterns = [
    path('lectures/',ListLecture.as_view(),name='lectures-list'),
    path('lectures/create',createLecture.as_view(),name='lecture-create'),
    path('lectures/<int:pk>/update',updateLecture.as_view(),name='update-lectures'),
    path('lectures/<int:pk>/delete',deleteLecture.as_view(),name='delete-lectures'),
    path('lectures/get_lectures_for_course/<int:course_id>/',getLecturesOfCourse,name='get_lectures_for_course'),
    path('instructor/<int:instructor_id>/lectures/', InstructorLectures.as_view(), name='instructor-lectures'),


    path('',include(router.urls))
]
