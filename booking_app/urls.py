from django.contrib import admin
from django.urls import path
from booking_app import views
from django.shortcuts import redirect

urlpatterns = [
    path('log_in/', views.log_in, name='login'),
    path('sign_up/', views.sign_up, name='signup'),
    path('places/', views.places_list, name='places_list'),
    path('booking/', views.booking, name='booking'),
    path('', lambda request: redirect('signup')),
]
