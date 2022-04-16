from django.test import TestCase
from migrate.models import Category, Post, User


class PostTestBase(TestCase):
    def setUp(self):
        return super().setUp()        

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)
    
    def make_author(
        self,
        first_name='user',
        last_name='name',
        username='username',
        password='123456',
        email='username@email.com',
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
        
    def make_post( 
        self,
        title = 'Post Title',
        description = 'Post Description',
        slug = 'post-slug',
        preparation_time = 10,
        preparation_time_unit = 'Minutos',
        servings=5,
        servings_unit = 'Pessoas',
        preparation_steps = 'Post Preparation Steps',
        preparation_steps_is_html = False,
        is_published = True,
        category_data = None,
        author_data = None,
    ):

        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data = {}
         
        return Post.objects.create(
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings=5,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
            category = self.make_category(**category_data),
            author = self.make_author(**author_data),
        )
