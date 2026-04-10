from django.test import TestCase, Client
from django.urls import reverse

class UnauthorizedPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_unauthorized_page_status_code(self):
        # The URL for unauthorized page is '/api/unauthorized' 
        # because the user_router is added to NinjaAPI at "" (root)
        # But wait, let's check precision_plastic_lab/api.py again
        # api.add_router("", user_router)
        # And precision_plastic_lab/urls.py
        response = self.client.get('/unauthorized')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'unauthorized.html')
        self.assertContains(response, 'Access Denied')
