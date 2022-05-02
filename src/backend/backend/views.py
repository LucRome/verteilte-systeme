from django.shortcuts import render
from django.shortcuts import redirect

def homepage(request):
    return redirect('person_list', page=1)
