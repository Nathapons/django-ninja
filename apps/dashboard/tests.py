from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class DashboardAuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.dashboard_url = reverse('api-1.0.0:get_dashboard_page')
        self.unauthorized_url = reverse('api-1.0.0:user_unauthorized_page')

    def test_dashboard_redirects_if_not_logged_in(self):
        response = self.client.get(self.dashboard_url)
        self.assertRedirects(response, self.unauthorized_url)

    def test_dashboard_accessible_if_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
