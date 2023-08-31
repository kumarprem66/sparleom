from django.db import models
from instructor.models import Instructor
from department.models import Department
# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=10,unique=True)
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='course_image/images',blank=True,null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name
