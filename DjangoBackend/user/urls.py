from django.urls import path

from .views import UserRegistration,UserLogin,UserDetails

urlpatterns = [
   path('register/', UserRegistration.as_view(), name='user-registration'),
   #  path('login/', UserLogin.as_view(), name='user-login'),
   path('login/', UserLogin.as_view(), name='user-login'),
    path('user-details/',UserDetails.as_view(), name='user-details'),

]