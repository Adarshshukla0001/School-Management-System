from django.db import models

# Create your models here.
class Student(models.Model):
    image=models.ImageField(upload_to='image/student_images/',max_length=250, null=True, default=None)
    stdid=models.CharField(max_length=40,primary_key=True)
    stdname=models.CharField(max_length=50)
    branch=models.CharField(max_length=40)
    dob=models.DateField()
    about=models.CharField(max_length=400)
    mobile=models.IntegerField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    qua=models.CharField(max_length=50)
    exp=models.CharField(max_length=10)
class Leave(models.Model):
    fid=models.CharField(max_length=20,primary_key=True)
    fname=models.CharField(max_length=50)
    department=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    fr=models.CharField(max_length=20)
    to=models.CharField(max_length=20)
    status=models.IntegerField()
    msg=models.CharField(max_length=100)  
class Feed(models.Model):
    fid=models.CharField(max_length=20,primary_key=True)
    fname=models.CharField(max_length=50)
    department=models.CharField(max_length=20)
    feedtype=models.CharField(max_length=20)
    msg=models.CharField(max_length=100)      
class SNfc(models.Model):
    nfcid=models.CharField(primary_key=True,max_length=20)  
    nfc=models.CharField(max_length=200)    
class SAttend(models.Model):
    stdid=models.CharField(primary_key=True,max_length=50)
    stdname=models.CharField(max_length=50)
    branch=models.CharField(max_length=40)
    date=models.CharField(max_length=20)
    status=models.IntegerField()     