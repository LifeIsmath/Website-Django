from django.urls import path

from migrate.views import home

from . import views

#pots:post
app_name = 'posts'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/search/', views.search, name="search"),
    path('posts/category/<int:category_id>/', 
        views.category, name="category"),
# ------------- Refactor -------------
    path('posts/<int:id>/', views.post, name="post"),
]
  