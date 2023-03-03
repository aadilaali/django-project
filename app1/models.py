from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=8)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
class Register1(models.Model):
    Name=models.CharField(max_length=15)
    Age=models.IntegerField()
    Place=models.CharField(max_length=15)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

class Gallery(models.Model):
    Name=models.CharField(max_length=15)
    Brand=models.CharField(max_length=15)
    Model=models.CharField(max_length=15)
    Price=models.IntegerField()
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
