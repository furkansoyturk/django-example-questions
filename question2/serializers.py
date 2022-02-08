from question2.models import Bin, Operation
from rest_framework import serializers


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['name', 'date']


class BinSerializer(serializers.ModelSerializer):
    # operation_name = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Bin
        # response fields
        fields = ['collection_frequency']
