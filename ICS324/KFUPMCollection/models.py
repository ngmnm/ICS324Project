from django.db import models
from django.utils import timezone


class department(models.Model):
    
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)



class dep(models.Model):
    
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)



# Create your models here.
