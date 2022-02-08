from django.db import models


# Create your models here.

class Bin(models.Model):
    last_collection = models.DateTimeField(auto_now_add=True, blank=True)
    collection_frequency = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Operation(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    bin = models.ForeignKey(Bin, related_name='operations', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
