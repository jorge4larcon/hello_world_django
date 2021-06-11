from django.urls import path

from webpages.views import hello_world_view


app_name = 'webpages'
urlpatterns = [ 
    path('', hello_world_view, name='hello_world'),
]
