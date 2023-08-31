from django.db import models
from course.models import Course
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)  # You can use PhoneNumberField if you've configured it
    course_ids = models.ManyToManyField(Course, blank=True)
