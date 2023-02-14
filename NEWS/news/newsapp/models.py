from django.db import models


class News(models.Model):
    title=models.CharField(max_length=100)
    news_desc=models.TextField()
    file_to=models.FileField(upload_to="media",null=True,default=None)

    def __str__(self):
        return self.title