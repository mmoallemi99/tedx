from rest_framework import viewsets, views

from events.serializers import (
    EventSerializer,
    StaffSerializer,
    SpeakerSerializer,
    SponsorSerializer,
)
from events.models import (
    Event,
    Staff,
    Speaker,
    Sponsor,
)


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        request = self.request
        qs = Speaker.objects.all()
        query = request.GET.get('status')
        if query is not None:
            qs = qs.filter(account_status__exact=query)
        return qs


class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

