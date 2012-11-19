from django.db import models


class Devotional(models.Model):
    title = models.CharField(max_length=250)
    month = models.IntegerField()
    day = models.IntegerField()
    body = models.TextField(max_length=1000)
