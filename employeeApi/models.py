from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)