from django.db import models
from course.models import Course
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=100)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    date_of_birth = models.DateField()
    contact_number = PhoneNumberField()  # You can use PhoneNumberField if you've configured it
    course_ids = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name