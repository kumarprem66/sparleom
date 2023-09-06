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
    email = models.EmailField(unique=True)
    contact_number = PhoneNumberField()
    password = models.CharField(max_length=128)
    experience = models.IntegerField(default=None)
    qualification = models.CharField(max_length=100,default=None)
    expertise = models.CharField(max_length=100,default=None)
    biodata = models.ImageField(upload_to='instruc_biaodata/images',blank=True,null=True,default=None)
    expected_salary = models.IntegerField(default=None)


    def __str__(self):
        return self.name
    