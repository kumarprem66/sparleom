
from django.contrib import admin
from django.urls import path
from .views import InstructorCreateAPIView,InstructorListAPIView,InstructorDeleteAPIView,InstructorUpdateAPIView

urlpatterns = [
    path('instructors/', InstructorListAPIView.as_view(),name='instructor-list'),
    path('instructors/create/',InstructorCreateAPIView.as_view(),name='instructor-create'),
    path('instructors/<int:pk>/update/',InstructorUpdateAPIView.as_view(),name='instructor-update'),
    path('instructors/<int:pk>/delete/',InstructorDeleteAPIView.as_view(),name='instructor-delete'),

]
