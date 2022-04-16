from django.test import TestCase
from django.urls import reverse


class PostURLsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('posts:home')
        self.assertEqual(url, '/')

    def test_category_url_is_correct(self):
        url = reverse('posts:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/post/category/1/')

        
    def test_detail_url_is_correct(self):
        url = reverse('posts:post', kwargs={'id': 1})
        self.assertEqual(url, '/post/1/')
