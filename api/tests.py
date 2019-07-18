from rest_framework.test import (
    APIClient,
    APITestCase,
    RequestsClient,
    APILiveServerTestCase
)
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse

from events.models import Event


class EventViewSetUnitTest(APITestCase):

    def setUp(self):
        self.event = Event.objects.create(name='TEDx UI 2019')
        self.client = APIClient()

    def test_can_retrieve_event(self):
        event = Event.objects.get()
        response = self.client.get(
            api_reverse('api:event-detail', kwargs={
                'pk': event.id,
            }),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, event)


class EventViewSetClientTest(APILiveServerTestCase):

    def setUp(self):
        self.event = Event.objects.create(
            name='TEDx 2019',
            year=2019,
        )

        self.client = RequestsClient()
        response = self.client.get(self.live_server_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_retrieve_events(self):
        events_url = self.live_server_url + '/events/'
        client = self.client
        response = client.get(events_url)
        valid_event_data = {
                'url': 'http://testserver/events/' + str(self.event.id) + '/',
                'name': self.event.name,
                'year': self.event.year,
                'staff_set': [],
            }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(valid_event_data, response.json())

# class StaffViewSetTest(APITestCase):
#
#     def setUp(self):
