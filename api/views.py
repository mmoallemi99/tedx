from rest_framework import viewsets

from events.serializers import EventSerializer, StaffSerializer
from events.models import Event, Staff


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

