from django.urls import resolve , reverse
from django.test import SimpleTestCase , TestCase
from .views import registration
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, registration)