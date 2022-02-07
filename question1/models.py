from django.db import models


# Create your models here.
class Vehicle(models.Model):
    # id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10)
    #
    # @classmethod
    # def get_new(cls):
    #     return cls.objects.get().id


class NavigationRecord(models.Model):
    # id = models.AutoField(primary_key=True)
    # vehicle = models.ForeignKey(Vehicle, default=Vehicle.get_new, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

