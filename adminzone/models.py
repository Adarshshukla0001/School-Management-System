from django.db import models

# Create your models here.
class Facalty(models.Model):
    image = models.ImageField(upload_to='image/faculty_images/',max_length=250, null=True, default=None )
    fid=models.CharField(max_length=40,primary_key=True)
    fname=models.CharField(max_length=50)
    department=models.CharField(max_length=40)
    about=models.CharField(max_length=400)
    salary=models.IntegerField()
    mobile=models.IntegerField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    qua=models.CharField(max_length=50)
    exp=models.CharField(max_length=10)
class Nfc(models.Model):
    nfcid=models.CharField(primary_key=True,max_length=20)  
    nfc=models.CharField(max_length=200)
class Attend(models.Model):
    fid=models.CharField(primary_key=True,max_length=50)
    fname=models.CharField(max_length=50)
    department=models.CharField(max_length=40)
    date=models.CharField(max_length=20)
    status=models.IntegerField()   
class Salary(models.Model):
    fid=models.CharField(primary_key=True,max_length=20)
    fname=models.CharField(max_length=50)
    department=models.CharField(max_length=40)
    salary=models.CharField(max_length=30)
    date=models.CharField(max_length=20)
    status=models.IntegerField()                 