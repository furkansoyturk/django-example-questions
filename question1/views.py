from datetime import datetime, timedelta

# Create your views here.
from rest_framework import viewsets
from question1.models import NavigationRecord
from question1.serializers import NavigationRecordSerializer


class NavigationRecordViewSet(viewsets.ModelViewSet):
    # find last two days and assign
    last_two_days = datetime.now() - timedelta(days=2)
    # filter result according to time
    queryset = NavigationRecord.objects.filter(datetime__range=(last_two_days.date(), datetime.now()))
    serializer_class = NavigationRecordSerializer
