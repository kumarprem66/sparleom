from django.db import models

from student.models import Student
from instructor.models import Instructor
# Create your models here.

class Ticket(models.Model):

    REASON_CHOICES = [
        ('Leave', 'Leave'),
        ('Assignment', 'Assignment'),
        ('Support', 'Support'),
    ]


    title = models.CharField(max_length=100)
    reason = models.CharField(max_length=20,choices=REASON_CHOICES)
    description = models.TextField()
    attachment = models.ImageField(upload_to='ticket/images',blank=True,null=True,default=None)
    studentId = models.ForeignKey(Student,on_delete=models.CASCADE)
    instructorId = models.ForeignKey(Instructor,on_delete=models.CASCADE)


    def __str__(self):
        return self.title