from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('erp:index'))
        self.assertEqual(response.status_code, 200)
