from django.db import models

class Student(models.Model):
    sid = models.IntegerField()
    name =models.CharField(max_length=200)
    roll = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name

