from django.urls import path
from .views import CourseListCreateView, CourseListView,CourseListUpdateView,CourseListDeleteView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/create/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/update', CourseListUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete', CourseListDeleteView.as_view(), name='course-delete'),
]