from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from department.models import Department

# Create your models here.

class Instructor(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
 
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    data_of_birth = models.DateField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    email = models.EmailField()
    contact_number = PhoneNumberField()
    password = models.CharField(max_length=128)
  

    def __str__(self):
        return self.name
    