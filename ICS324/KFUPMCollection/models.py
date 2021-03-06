from django.db import connections
from django.db import models
from django.utils import timezone


class departments(models.Model):

    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    DID = models.CharField(max_length=250)

    class Meta:
        db_table = "department"


class course(models.Model):

    Name = models.CharField(max_length=250)
    CID = models.CharField(max_length=250)
    prerequisites = models.CharField(max_length=250)
    DID = models.CharField(max_length=250)

    class Meta:
        db_table = "course"

class resource(models.Model):

    Name = models.CharField(max_length=250)
    RID = models.CharField(max_length=250)
    Type = models.CharField(max_length=250)
    CID = models.CharField(max_length=250)
    path = models.FileField(upload_to='KFUPMCollection/static/upload/', max_length=100)

    class Meta:
        db_table = "resource"


class evaluation(models.Model):

    EID = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)
    E_Date = models.CharField(max_length=250)
    SID = models.CharField(max_length=250)
    IID = models.CharField(max_length=250)

    class Meta:
        db_table = "evaluation"

class instructor(models.Model):

    Name = models.CharField(max_length=250)
    IID = models.CharField(max_length=250)
    Office_Phone_number = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Office_location = models.CharField(max_length=250)
    website = models.CharField(max_length=250)

    class Meta:
        db_table = "instructor"

class workFor(models.Model):

    DID = models.CharField(max_length=250)
    IID = models.CharField(max_length=250)

    class Meta:
        db_table = "work_for"

class answer(models.Model):

    AID = models.CharField(max_length=250)
    Rate = models.CharField(max_length=250)
    QID = models.CharField(max_length=250)
    EID = models.CharField(max_length=250)
    

    class Meta:
        db_table = "answer"

class question(models.Model):

    QID = models.CharField(max_length=250)
    Weight = models.CharField(max_length=250)
    Qname = models.CharField(max_length=250)

    class Meta:
        db_table = "question"

class work_for(models.Model):

    IID = models.CharField(max_length=250)
    DID = models.CharField(max_length=250)

    class Meta:
        db_table = "work_for"

class contains(models.Model):

    QID = models.CharField(max_length=250)
    EID = models.CharField(max_length=250)

    class Meta:
        db_table = "contains"


class dep(models.Model):

    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)