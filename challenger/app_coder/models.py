from django.db import models

# Create your models here.
class Member (models.Model):

    name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    dni = models.IntegerField()
    birthday = models.DateField()