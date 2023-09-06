from rest_framework.routers import DefaultRouter
from .views import TicketCrud,StudentTickets,InstructorTickets
from django.urls import path,include


router = DefaultRouter()
router.register(r'tickets',TicketCrud)

urlpatterns = [
    
    path('',include(router.urls)),
    path('student/<int:student_id>/tickets/', StudentTickets.as_view(), name='student-tickets'),
    path('instructor/<int:instructor_id>/tickets/', InstructorTickets.as_view(), name='instructor-tickets'),
]