from django.db import connections
from django.db import models
from django.utils import timezone


class departments(models.Model):

    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)

    class Meta:
        db_table = "department"


class course(models.Model):

    Name = models.CharField(max_length=250)
    CID = models.CharField(max_length=250)
    prerequisites = models.CharField(max_length=250)
    DID = models.CharField(max_length=250)

    class Meta:
        db_table = "course"

class instructor(models.Model):

    Name = models.CharField(max_length=250)
    IID = models.CharField(max_length=250)
    Office_Phone_number = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Office_location = models.CharField(max_length=250)
    website = models.CharField(max_length=250)

    class Meta:
        db_table = "instructor"


class dep(models.Model):

    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)


# Create your models here.
