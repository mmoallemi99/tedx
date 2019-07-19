from rest_framework import serializers

from .models import (
    Event,
    Staff,
    Speaker,
)


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:staff-detail',
    )
    event = serializers.HyperlinkedRelatedField(
        view_name='api:event-detail',
        read_only=True
    )

    class Meta:
        model = Staff
        fields = '__all__'


class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:speaker-detail',
    )
    event = serializers.HyperlinkedRelatedField(
        view_name='api:event-detail',
        read_only=True,
    )

    class Meta:
        model = Speaker
        fields = '__all__'


class EventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:event-detail',
    )
    staff_set = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


