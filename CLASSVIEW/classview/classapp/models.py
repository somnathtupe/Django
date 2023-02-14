from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    pages = models.IntegerField()
    code = models.IntegerField()

    def __str__(self):
        return '%s - %s  ' % (self.author.name,self.title)