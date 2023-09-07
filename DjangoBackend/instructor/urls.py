
from django.contrib import admin
from django.urls import path,include
from .views import InstructorCreateAPIView,InstructorListAPIView,InstructorDeleteAPIView,InstructorUpdateAPIView,SingleInstructor,InstructorLogin
from rest_framework.routers import DefaultRouter

# from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'instructors',SingleInstructor)


urlpatterns = [
    path('instructors/', InstructorListAPIView.as_view(),name='instructor-list'),
    path('instructors/create',InstructorCreateAPIView.as_view(),name='instructor-create'),
    path('instructors/<int:pk>/update',InstructorUpdateAPIView.as_view(),name='instructor-update'),
    path('instructors/<int:pk>/delete',InstructorDeleteAPIView.as_view(),name='instructor-delete'),

    path('',include(router.urls)),
    # path('instructors/login',obtain_auth_token,name='instructor-login'),
     path('instructors/login/', InstructorLogin.as_view(), name='instructor-login'),

]
