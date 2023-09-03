
from django.contrib import admin
from django.urls import path
from .views import DepartmentListCreateView,DepartmentListAPIView

urlpatterns = [
    path('departments/create', DepartmentListCreateView.as_view(),name='department-list-create'),
    path('departments/',DepartmentListAPIView.as_view(),name='department-list')

]
