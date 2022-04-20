from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_post_base import Post, PostTestBase


class PostModelTest(PostTestBase):
    def setUp(self):
        self.post = self.make_post()
        return super().setUp()
    
    def test_post_title_raises_error_if_title_has_more_chars(self):
        self.post.title = 'A' * 70
        
        with self.assertRaises(ValidationError):
            self.post.full_clean()
    
    def make_post_no_defaults(self):
            post = Post(
                category = self.make_category(name='Test Default Category'),
                author = self.make_author(username='newuser'),
                title = 'Post Title',
                description = 'Post Description',
                slug = 'post-slug-for-no-defaults',
                preparation_time = 10,
                preparation_time_unit = 'Minutos',
                servings=5,
                servings_unit = 'Pessoas',
                preparation_steps = 'Post Preparation Steps',
            )
            post.full_clean()
            post.save()
            return post
    
    @parameterized.expand([
            ('title', 65),
            ('description', 165), 
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
    ])   
    def test_post_fields_max_length(self, field, max_length):
            setattr(self.post, field, 'A' * (max_length + 1))
            with self.assertRaises(ValidationError):
                self.post.full_clean()
                
# ---- Test Preparation Post -----------------------------------------------
    def test_post_preparation_steps_is_html_is_false_by_default(self):
            post = self.make_post_no_defaults()
            self.assertFalse(
                post.preparation_steps_is_html, 
                msg='Post preparation_steps_is_html is not False',
                             
            )
# ---------------------------------------------------------------------------

    def test_post_is_published_is_false_by_default(self):
            post = self.make_post_no_defaults()
            self.assertFalse(
                post.is_published, 
                msg='Post is_published is not False',                             
            )
            
    def test_post_string_representation(self):
        needed = 'Testing Representation'
        self.post.title = needed
        self.post.full_clean()
        self.post.save()
        self.assertEqual(
            str(self.post), needed,
            msg=f'''Post string representation must be
                    {needed} but {str(self.post)} was received'''                
            )
