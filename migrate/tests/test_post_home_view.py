from re import S

from django.urls import resolve, reverse
from migrate import views

from .test_post_base import Post, PostTestBase


class PostHomeViewsTest(PostTestBase):
    
    def test_post_home_view_functions_is_correct(self):
        view = resolve(reverse('posts:home')) 
        self.assertIs(view.func, views.home)

    def test_post_home_view_loads_correct_template(self):
        response = self.client.get(reverse('posts:home'))
        self.assertTemplateUsed(response, 'migrate/pages/home.html')
        
    def test_post_home_template_shows_no_posts_found_if_no_posts(self):
        response = self.client.get(reverse('posts:home'))
        self.assertIn(
            'No posts found',  
            response.content.decode('utf-8')
        )
        
    def test_post_home_template_dont_load_posts_not_published(self):
        # Need a post for this test
        """"test posts is_published False don't show"""
        
        self.make_post(is_published=False)
        
        response = self.client.get(reverse('posts:home'))        
    
        self.assertIn(
            'No posts found',  
            response.content.decode('utf-8')
        )
    
