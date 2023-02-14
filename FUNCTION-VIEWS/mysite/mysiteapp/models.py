from django.db import models
from django.contrib.auth.models import User 

class Food(models.Model):

    name=models.CharField(max_length=200)
    carbs=models.FloatField()
    protein= models.FloatField()
    flat=models.FloatField()
    calaries=models.IntegerField()

    def __str__(self):
        return self.name


class Consume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed=models.ForeignKey(Food,on_delete=models.CASCADE)