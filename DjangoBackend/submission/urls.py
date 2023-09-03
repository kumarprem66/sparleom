from django.urls import path
from .views import SubmissionCreate,SubmissionList

urlpatterns = [
    path('submission/create',SubmissionCreate.as_view(),name='submission-create'),
    path('submission/',SubmissionList.as_view(),name='submissions'),
]