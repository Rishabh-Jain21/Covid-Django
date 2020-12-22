from covidapp.views import covid_tracker_view
from django.contrib import admin
from django.urls import path, include
from .views import covid_tracker_view
urlpatterns = [
    path('', covid_tracker_view)
]
