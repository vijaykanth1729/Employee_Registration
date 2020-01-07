from audioop import reverse

from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    emp_code = models.CharField(max_length=3)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

