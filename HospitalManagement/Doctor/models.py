from django.db import models

# Create your models here.
class Drname(models.Model):
    
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField(null=True)
    Special = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10,null=True)

class Patient(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10,null=True)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=150)

class Appoinment(models.Model):
    doctor = models.ForeignKey(Drname,on_delete=models.CASCADE)
    patient = models.CharField(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()