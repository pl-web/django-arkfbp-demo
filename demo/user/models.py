from django.db import models

# Create your models here.
class User(models.Model):
   name = models.CharField(max_length=100)
   age = models.IntegerField(default=0)
   identity = models.CharField(max_length=100)