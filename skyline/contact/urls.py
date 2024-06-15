
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('index/', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('checkin/', views.checkin_view, name='checkin'),
    path('manage/', views.checkin_view, name='manage'),
    path('flightstatus/', views.flightstatus_view, name='flightstatus'),
    path('contact_us/', views.contact_us_image, name='contact_us_image'),
]