from django.db import models

# Create your models here.. 
class Form(models.Model):
    name=models.CharField(max_length=100,null=True)
    age=models.IntegerField(default=0)
    dob=models.DateField(null=True,blank=True)
    fathername=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(default=0)
    email=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)

