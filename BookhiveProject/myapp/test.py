from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):

    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_login_page(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_book_detail_page(self):
        response = self.client.get('/book/1/')  # adjust if needed
        self.assertIn(response.status_code, [200, 404])
