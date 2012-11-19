from django.db import models

from taggit.managers import TaggableManager

class Devotional(models.Model):
    title = models.CharField(max_length=250)
    month = models.IntegerField()
    day = models.IntegerField()
    body = models.TextField(max_length=1000)


    tags = TaggableManager()