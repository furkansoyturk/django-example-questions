from question1.models import NavigationRecord
from rest_framework import serializers


class NavigationRecordSerializer(serializers.ModelSerializer):

    # get related vehicle plate from Vehicle model
    vehicle_plate = serializers.CharField(source='vehicle.plate')

    class Meta:
        model = NavigationRecord
        # response fields
        fields = ['vehicle_plate', 'datetime', 'latitude', 'longitude']
