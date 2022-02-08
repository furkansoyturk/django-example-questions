from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from question2.models import Bin
from question2.serializers import BinSerializer


class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.filter()
    serializer_class = BinSerializer
