from question2.models import Bin
from rest_framework import serializers


class BinSerializer(serializers.ModelSerializer):

    # get related vehicle plate from Vehicle model
    # vehicle_plate = serializers.CharField(source='vehicle.plate')

    class Meta:
        model = Bin
        # response fields
        fields = ['collection_frequency']
