from django.urls import path
from .views import StudentListView,StudentCreateView,StudentDeleteView,StudentUpdateView,AddCourseToStudent

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
urlpatterns = [

    path('student/create',StudentCreateView.as_view(),name='student-create'),
    path('student/',StudentListView.as_view(),name='student-list'),
    path('student/<int:pk>/update',StudentUpdateView.as_view(),name='student-update'),
    path('student/<int:pk>/delete',StudentDeleteView.as_view(),name='student-delete'),
    path('', include(router.urls)),
    path('students/<int:pk>/add-course/', AddCourseToStudent.as_view(),name="update-student-course"),
]