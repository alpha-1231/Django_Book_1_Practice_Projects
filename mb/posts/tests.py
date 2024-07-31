from django.test import TestCase
from .models import Post
from django.urls import reverse

class Post_Model_Test(TestCase):
    def setup(self):
        Post.objects.create(text='aabbcc')
    def the_main_test(self):
        post = Post.objects.get(id=1)
        expected = f'{post.text}'
        self.assertEqual(expected,'aabbcc')
        
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='abc')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
    def test_view_uses_the_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertTemplateUsed(resp,'home.html')
        
    