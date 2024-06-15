# skyline/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')),  # This will include all the paths defined in contact/urls.py
]
