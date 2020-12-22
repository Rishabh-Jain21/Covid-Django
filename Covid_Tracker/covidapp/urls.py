from covidapp.views import helloworldview
from django.contrib import admin
from django.urls import path, include
from .views import helloworldview
urlpatterns = [
    path('', helloworldview)
]
