from django.test import TestCase
from django.urls import resolve, reverse
from cv.views import cv1
from django.http import HttpRequest

# Create your tests here.


class HomePageTest(TestCase):

       def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv1(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>CV</title>', html)  
        self.assertTrue(html.endswith('</html>'))  