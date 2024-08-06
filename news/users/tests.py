from django.test import TestCase
from django.test import SimpleTestCase,TestCase
from django.urls import reverse 
from django.contrib.auth import get_user_model
# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_1(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_2(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'
    
    def test_1(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code,200)
        
    def test_2(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'signup.html')
        
    def test_3(self):
        new_user = get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)