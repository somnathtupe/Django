from django.db import models
from django.contrib.auth import get_user_model 


class Book(models.Model):

    TYPE_PHYSICAL= 'physical'
    TYPE_VIRTUAL= 'virtual'
    TYPE_CHOICES=(
        (TYPE_PHYSICAL,'physical'),
        (TYPE_VIRTUAL,'virtual')
    )

    type = models.CharField(max_length=20,choices=TYPE_CHOICES,default='')
    # Common attribute 

    name = models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField(help_text='in ruppes')
  
    # Special character
    weight= models.PositiveBigIntegerField(help_text='gram')
    download_link=models.URLField(null=True,blank=True)

    def __str__(self) :
       return f'[{self.get_type_display()}] {self.name}'


class Cart(models.Model):
    user=models.OneToOneField(get_user_model(),primary_key=True,on_delete=models.CASCADE)
    books=models.ManyToManyField(Book)