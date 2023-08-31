
from django.contrib import admin
from django.urls import path
from .views import DepartmentListCreateView,DepartmentListAPIView

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(),name='department-list-create'),
    path('departments/list/',DepartmentListAPIView.as_view(),name='department-list')

]
