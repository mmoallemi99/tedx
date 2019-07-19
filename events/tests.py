from django.test import TestCase

from .models import (
    Event,
    Staff,
    Speaker,
)


# Event
# Event --> Staff
# Event --> Speaker

# Event --> Sponsor
# Event --> Sponsor --> Register Form

# Slider


class EventModelTest(TestCase):

    def test_saving_and_retrieving_events(self):
        new_event = Event.objects.create(name='TEDx UI 2019')
        saved_event = Event.objects.first()

        self.assertEqual(new_event, saved_event)


class StaffModelTest(TestCase):

    def test_saving_and_retrieving_staffs(self):
        new_event = Event.objects.create(name='TEDx UI 2019')
        new_staff = Staff.objects.create(event=new_event, name='mohammad moallemi')

        saved_event = Event.objects.first()
        saved_staff = Staff.objects.first()

        self.assertEqual(saved_event, new_event)
        self.assertEqual(saved_staff, new_staff)


class SpeakerModelTest(TestCase):

    def test_saving_and_retrieving_speakers(self):
        new_event = Event.objects.create(name='TEDx 2019')
        new_speaker = Speaker.objects.create(event=new_event, name='Masoud Algoone')

        saved_event = Event.objects.first()
        saved_speaker = Speaker.objects.first()

        self.assertEqual(new_event, saved_event)
        self.assertEqual(new_speaker, saved_speaker)

