from .views import *
from django.urls import path

urlpatterns = [
    path('page<int:page>', person_list, name='person_list'),
    path('new', new_person, name='new_person'),
    path('delete/<int:id>', delete_person, name='delete_person')
]