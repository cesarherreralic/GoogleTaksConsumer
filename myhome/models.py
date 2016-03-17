from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)

