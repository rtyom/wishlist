from django.urls import path

from .views import *

urlpatterns = [
    path('', women_index),
    path('categories/', women_cats)
]