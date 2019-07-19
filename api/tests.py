from rest_framework.test import (
    APIClient,
    APITestCase,
    RequestsClient,
    APILiveServerTestCase,
)
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse

from .utils import test_image_generator

from events.models import Event, Staff


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


class EventAPIClientTest(APILiveServerTestCase):

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


class StaffViewSetClientTest(APITestCase):

    def setUp(self):
        self.event = Event.objects.create(name='TEDx 2019')

        from PIL import Image
        from io import BytesIO
        tmp_file = BytesIO(b'fake file stream for test')
        image = Image.new('RGB', (10, 10))
        temp_file = image.save(tmp_file, format='png')
        self.staff = Staff.objects.create(
            event=self.event,
            name='Mohammad Moallemi',
            role='programmer',
            picture=temp_file,
        )

        self.client = APIClient()

    def test_can_retrieve_staff(self):
        staff = Staff.objects.get()
        response = self.client.get(
            api_reverse('api:staff-detail', kwargs={
                'pk': staff.id
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, staff)


class StaffAPIClientTest(APILiveServerTestCase):

    def setUp(self):
        self.event = Event.objects.create(name='TEDx 2019')

        image = test_image_generator()
        self.staff = Staff.objects.create(
            event=self.event,
            name='Mohammad Moallemi',
            role='programmer',
            picture=image,
        )

        self.client = RequestsClient()
        response = self.client.get(self.live_server_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_retrieve_staffs(self):
        staff_url = self.live_server_url + '/staffs/'
        client = self.client
        response = client.get(staff_url)

        image = test_image_generator()
        valid_staff_data = {
            'url': 'http://testserver/staffs/' + str(self.staff.id) + '/',
            'name': self.staff.name,
            'event': 'http://testserver/events/' + str(self.staff.event.id) + '/',
            'role': self.staff.role,
            'picture': image,
            'bio': None,
            'linkedin_account': None,
            'github_account': None,
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(valid_staff_data, response.json())
