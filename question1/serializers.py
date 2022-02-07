from django.contrib.auth.models import User, Group
from question1.models import Vehicle, NavigationRecord
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class VehicleSerializer(serializers.RelatedField):
#     def get_plates(self, value):
#         plate = value.plate
#         return plate
#
#     class Meta:
#         model = Vehicle


class NavigationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationRecord
        fields = ['vehicle', 'datetime', 'latitude', 'longitude']
