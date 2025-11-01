from django.db import models

# Create your models here.
class ad(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
class Contact(models.Model):
    mobile=models.IntegerField()
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=10)
    msg=models.CharField(max_length=300)        