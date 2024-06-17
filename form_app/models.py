from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.author
