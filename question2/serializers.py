from question2.models import Bin, Operation
from rest_framework import serializers


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        # response fields
        fields = ['name', 'date']


class BinSerializer(serializers.ModelSerializer):
    # bin - operation relationship (one to many)
    operations = OperationSerializer(many=True, read_only=True)

    # counting relationship between bin and operation to calculate collection frequency
    collection_frequency = serializers.IntegerField(
        source='operations.count',
        read_only=True
    )

    class Meta:
        model = Bin
        # response fields
        fields = ['id', 'collection_frequency', 'operations']
