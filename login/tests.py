from django.urls import resolve , reverse
from django.test import SimpleTestCase , TestCase
from .views import loginfn
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, loginfn)
    