from rest_framework.test import APIClient
from rest_framework import status

from django.test import TestCase
from django.urls import reverse

from events.models import Event


class EventViewSetTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(name='TEDx UI 2019')
        self.client = APIClient()

    def test_can_retrieve_event(self):
        event = Event.objects.get()
        response = self.client.get(
            reverse('api:event'),
            kwargs={
                'id': event.id,
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, event)



