from django.urls import path

from migrate.views import home

urlpatterns = [
    path('', home),

]
