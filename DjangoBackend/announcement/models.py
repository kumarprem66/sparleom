from django.db import models

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date  = models.DateField()

    def __str__(self):
        return self.title
