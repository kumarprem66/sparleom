from django.urls import path
from .views import EnrollmentListView,EnrollmentListCreateView

urlpatterns = [
    path('enrollment/create',EnrollmentListCreateView.as_view(),name='enrollment-create'),
    path('enrollments',EnrollmentListView.as_view(),name='enrollments'),
]