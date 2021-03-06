from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class LegalTemplateViewTest(TestCase):
    """
    testing legal notice page
    """
    def test_legal_page_status_code(self):
        response = self.client.get(reverse('legal'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mentions légales")
        self.assertTemplateUsed(response, 'legal_notice/notice.html')
