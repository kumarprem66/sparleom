from django.urls import path

from .views import UserCreate,UserList

urlpatterns = [
    path('userregis',UserCreate.as_view(), name='user-regis'),
    path('users/',UserList.as_view(), name='user-list'),
    
]