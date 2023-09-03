from django.urls import path
from .views import AnnounceCreate,AnnounceDelete,AnnounceList,AnnounceUpdate

urlpatterns = [
    path('announces/',AnnounceList.as_view(),name='announce-list'),
    path('announces/create',AnnounceCreate.as_view(),name='announce-create'),
    path('announces/<int:pk>/update',AnnounceUpdate.as_view(),name='announce-update'),
    path('announces/<int:pk>/delete',AnnounceDelete.as_view(),name='announce-delete'),
]