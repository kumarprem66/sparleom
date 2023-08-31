from django.urls import path
from .views import AsignmentCreate,AsignmentList,AsignmentDelete,AsignmentUpdate


urlpatterns = [
    path('assignment/create/',AsignmentCreate.as_view(),name='assignment-create'),
    path('assignments/',AsignmentCreate.as_view(),name='assignments'),
    path('assignment/<int:pk>/update',AsignmentCreate.as_view(),name='assignment-update'),
    path('assignment/<int:pk>/delete',AsignmentCreate.as_view(),name='assignment-delete'),
]