from django.db import models 

# Create your models here.

class Job(models.Model):
    jobid = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    remote = models.BooleanField()
    
class Language(models.Model):
    languageid = models.IntegerField()
    name = models.CharField(max_length=50)
    jobid = models.IntegerField()