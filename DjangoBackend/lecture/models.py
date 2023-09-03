from django.db import models
from course.models import Course

# Create your models here.

class Lecture(models.Model):
    lecture_course_name = models.ForeignKey(Course,on_delete=models.CASCADE,default=2)
    topic_title = models.CharField(max_length=100)
    timing = models.DateTimeField()
    meeting_url = models.URLField()

    def __str__(self):
        return self.topic_title
