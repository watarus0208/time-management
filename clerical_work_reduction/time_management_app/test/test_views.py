from django.test import TestCase
from django.urls import reverse


class LoginViewTests(TestCase):
    def test_status_code(self):
        url = reverse('time_management_app:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class SinupViewTests(TestCase):
    def test_status_code(self):
        url = reverse('time_management_app:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
