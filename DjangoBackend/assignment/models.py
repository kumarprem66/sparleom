from django.db import models
from course.models import Course
from datetime import datetime
# Create your models here.


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructon = models.TextField(default=None)
    start_date = models.DateTimeField(default=datetime.now)
    due_date = models.DateField()

    def __str__(self):
        return self.title
