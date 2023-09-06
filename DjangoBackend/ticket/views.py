from django.shortcuts import render
from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer
# Create your views here.

class TicketCrud(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer



# views.py



class StudentTickets(APIView):
    def get(self, request, student_id):
        try:
            # Get all tickets associated with the student
            tickets = Ticket.objects.filter(studentId=student_id)

            # Serialize ticket data
            serializer = TicketSerializer(tickets, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Ticket.DoesNotExist:
            return Response(
                {"message": "Tickets not found for this student."},
                status=status.HTTP_404_NOT_FOUND
            )

class InstructorTickets(APIView):
    def get(self, request, instructor_id):
        try:
            # Get all tickets associated with the instructor
            tickets = Ticket.objects.filter(instructorId=instructor_id)

            # Serialize ticket data
            serializer = TicketSerializer(tickets, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Ticket.DoesNotExist:
            return Response(
                {"message": "Tickets not found for this instructor."},
                status=status.HTTP_404_NOT_FOUND
            )

