from django.db import models

# Create your models here.
class fun(models.Model):
    p_name =  models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    cell = models.IntegerField(null=True)