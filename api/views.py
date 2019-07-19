from rest_framework import viewsets

from events.serializers import (
    EventSerializer,
    StaffSerializer,
    SpeakerSerializer,
)
from events.models import (
    Event,
    Staff,
    Speaker,
)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

