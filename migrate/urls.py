from django.urls import path

from migrate.views import home

from . import views

#pots:post
app_name = 'posts'

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:id>/', views.post, name="post"),

]
  