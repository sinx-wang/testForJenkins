from django.db import models

# Create your models here.
class Person(models.Model):
    userId=models.CharField(max_length=10)
    userPw=models.CharField(max_length=10)
