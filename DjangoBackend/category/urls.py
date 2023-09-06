from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryCrud
router = DefaultRouter()
router.register(r'category',CategoryCrud)


urlpatterns=[

    path('',include(router.urls))
]