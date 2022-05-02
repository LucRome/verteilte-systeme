from .views import *
from django.urls import path

urlpatterns = [
    path('persons/page<int:page>', person_list, name='person_list')
]