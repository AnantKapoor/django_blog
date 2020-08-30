from django.test import TestCase
from django.urls import resolve, reverse
from cv.views import cv1
from django.http import HttpRequest
from datetime import datetime
from django.utils.timezone import make_aware
from cv.models import Education, Experience, Skills, Interests

# Create your tests here.


class HomePageTest(TestCase):

       def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv1(request)  
        html = response.content.decode('utf8')  
        self.assertIn('<title>CV</title>', html)  
        self.assertTrue(html.endswith('</html>'))  

class TestEducation(TestCase):

       def setUp(self):
              Education.objects.create(title = "TestTitle" , grades='TestGrade', description='TestString', graduation_date=datetime(2020, 5, 13, 22, 50, 55))

       def test_education(self):
              test_education= Education.objects.get(title = "TestTitle")
              self.assertEqual(test_education.grades ,"TestGrade")
              self.assertEqual(test_education.description ,"TestString")
              self.assertEqual(test_education.graduation_date ,make_aware(datetime(2020, 5, 13, 22, 50, 55)))

class TestExperience(TestCase):

       def setUp(self):
              Experience.objects.create(title = "TestTitle" , position='TestPosition', text='TestString', start_date=datetime(2020, 5, 13, 22, 50, 55), end_date=datetime(2020, 5, 13, 22, 50, 55))

       def test_experience(self):
              test_experience = Experience.objects.get(title = "TestTitle")
              self.assertEqual(test_experience.position ,"TestPosition")
              self.assertEqual(test_experience.text ,"TestString")
              self.assertEqual(test_experience.start_date ,make_aware(datetime(2020, 5, 13, 22, 50, 55)))
              self.assertEqual(test_experience.end_date ,make_aware(datetime(2020, 5, 13, 22, 50, 55)))

class TestSkills(TestCase):

       def setUp(self):
              Skills.objects.create(title = "TestTitle" , description='TestString')

       def test_skills(self):
              test_skills = Skills.objects.get(title = "TestTitle")
              self.assertEqual(test_skills.description ,"TestString")


          
class TestInterest(TestCase):
       def setUp(self):
              Interests.objects.create(title='TestTitle')

       def test_interest(self):
              Interests.objects.get(title = "TestTitle")


