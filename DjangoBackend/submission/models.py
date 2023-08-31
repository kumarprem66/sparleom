from django.db import models
from student.models import Student
from assignment.models import Assignment
# Create your models here.

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    STATUS_CHOICES = [
        ("Submitted", "Submitted"),
        ("Late", "Late"),
        ("Graded", "Graded"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.student} - {self.assignment}"