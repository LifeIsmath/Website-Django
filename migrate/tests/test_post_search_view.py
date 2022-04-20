from re import S

from django.urls import resolve, reverse
from migrate import views

from .test_post_base import Post, PostTestBase


class PostViewsTest(PostTestBase):
    
    def test_post_search_uses_correct_view_function(self):
        resolved = resolve(reverse('posts:search'))
        self.assertIs(resolved.func, views.search)
    
    def test_post_search_loads_correct_template(self):
       response = self.client.get(reverse('posts:search') + '?q=teste')
       self.assertTemplateUsed(response, 'migrate/pages/search.html')
       
    def test_post_search_raises_404_if_no_search_term(self):
        url = reverse('posts:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_post_search_term_is_on_page_title_and_escaped(self):
        url = reverse('posts:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )
