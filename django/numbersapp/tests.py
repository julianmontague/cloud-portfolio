from unittest import TestCase
from django.test import RequestFactory, Client

# Create your tests here.
from .views import get_3, get_4, get_number

class NumberViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_get_3(self):
        request = self.factory.get('/number/3')
        response = get_3(request)
        self.assertEqual(response.content, b'3')
        self.assertEqual(response.status_code, 200)

    def test_get_4(self):
        response = self.client.get('/number/4')
        self.assertEqual(response.content, b'4')
        self.assertEqual(response.status_code, 200)

    def test_valid_get_number(self):
        response = self.client.get('/number/any/17')
        self.assertEqual(response.content, b'17')
        self.assertEqual(response.status_code, 200)

    def test_invalid_get_number(self):
        response = self.client.get('/number/any/-1')
        self.assertEqual(response.status_code, 400)
