from tkinter import CASCADE
from django.db import models

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    singer = models.ForeignKey(Singer, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title