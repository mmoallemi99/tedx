from rest_framework import serializers

from .models import Event, Staff


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:staff-detail',
        lookup_field='pk',
    )
    event = serializers.HyperlinkedIdentityField(
        view_name='api:event-detail',
        lookup_field='pk',
    )

    class Meta:
        model = Staff
        fields = '__all__'


class EventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:event-detail',
        lookup_field='pk',
    )
    staff_set = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('url',
                  'name',
                  'year',
                  'staff_set', )




