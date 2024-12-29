from django.db import models

# Create your models here.
class Food_items(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    
class Soft_drinks(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    Image = models.ImageField(null=True)

class Bill_Items(models.Model):
       Bill_no = models.IntegerField()
       Product_name = models.CharField(max_length=40)
       Total = models.IntegerField()
       Image = models.ImageField(null=True)