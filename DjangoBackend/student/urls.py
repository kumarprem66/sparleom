from django.urls import path
from .views import StudentListView,StudentCreateView,StudentDeleteView,StudentUpdateView


urlpatterns = [

    path('student/create',StudentCreateView.as_view(),name='student-create'),
    path('students',StudentListView.as_view(),name='student-list'),
    path('student/update',StudentUpdateView.as_view(),name='student-update'),
    path('student/delete',StudentDeleteView.as_view(),name='student-delete'),
]