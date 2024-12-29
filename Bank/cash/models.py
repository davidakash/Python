from django.db import models

# Create your models here.
class lucky(models.Model):
    Name = models.CharField(max_length=50)
    AccNo = models.IntegerField(null=False)
    
class boss(models.Model):
    bank = models.ForeignKey(lucky,null = True,on_delete = models.SET_NULL)
    TypeofAcc = models.CharField(max_length=50)
    image = models.ImageField(null = True)