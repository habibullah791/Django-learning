from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_templete_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,"<h1>This is home Page</h1>")

class AboutPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
            response = self.client.get("/about/")
            self.assertEqual(response.status_code, 200)
            
    def test_templete_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response,"<h1>This is About Page</h1>")
