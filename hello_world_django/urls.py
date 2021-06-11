from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('webpages.urls', namespace='webpages')),
    path('admin/', admin.site.urls),
]
