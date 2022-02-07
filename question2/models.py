from django.db import models


# Create your models here.

class Bin(models.Model):
    last_collection = models.DateTimeField(auto_now_add=True, blank=True)
    collection_frequency = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Operation(models.Model):
    bin_id = models.ForeignKey(Bin, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=True)
