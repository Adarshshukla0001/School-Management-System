from django.db import models

# Create your models here.
class Feed(models.Model):
    stdid=models.CharField(max_length=20,primary_key=True)
    stdname=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    feedtype=models.CharField(max_length=20)
    msg=models.CharField(max_length=100)    
class SLeave(models.Model):
    stdid=models.CharField(max_length=20,primary_key=True)
    stdname=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    fr=models.CharField(max_length=20)
    to=models.CharField(max_length=20)
    status=models.IntegerField()
    msg=models.CharField(max_length=100)    