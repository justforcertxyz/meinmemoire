from django.test import TestCase, Client
from django.urls import reverse


class IndexPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('landing:index')

    def test_index_page_returns_correct_response(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'landing/index.html')
        self.assertTemplateUsed(response, 'landing/base.html')
        self.assertEqual(response.status_code, 200)

    def test_index_page_returns_corrent_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, "<title>Home")


class PrivacyPolicyPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('landing:privacy-policy')

    def test_privacy_policy_page_returns_correct_response(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'landing/privacy_policy.html')
        self.assertTemplateUsed(response, 'landing/base.html')
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_page_returns_corrent_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, "<title>Datenschutzerklärung")
