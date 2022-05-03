from django.forms import model_to_dict
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .utils import get_value
from .forms import PersonFilterForm, PersonForm
from .models import Person

ELEMENTS_PER_SITE = 20

# Create your views here.
def person_list(request: HttpRequest, page=1):
    if request.method == 'POST':
        filter = PersonFilterForm(request.POST)
        if filter.is_valid():
            persons = Person.objects.filter(
                first_name__startswith=get_value(filter, 'first_name'),
                last_name__startswith=get_value(filter, 'last_name')
            )
    else:
        filter = PersonFilterForm()
        persons = Person.objects.all()
    
    paginator = Paginator(persons, ELEMENTS_PER_SITE)
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'filter_form': filter
    }

    return render(request, 'pages/person_list.html', context)

def new_person(request: HttpRequest):
    success = False
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    
    else:
        form = PersonForm()

    context = {
        'success': success,
        'form': form
    }

    return render(request, 'pages/create_person.html', context)

def delete_person(request: HttpRequest, id):
    person_to_delete = get_object_or_404(Person, pk=id)
    first_name = person_to_delete.first_name
    last_name = person_to_delete.last_name
    birthday = person_to_delete.birthday
    person_to_delete.delete()

    context =  {
        'first_name': first_name,
        'last_name': last_name,
        'birthday': birthday
    }

    return render(request, 'pages/delete_person.html', context)

def edit_person(request: HttpRequest, id):
    update_success = False
    if request.method == 'POST':
        person_obj = get_object_or_404(Person, pk=id)
        form = PersonForm(request.POST or None, instance=person_obj)
        if form.is_valid():
            form.save()
            update_success = True
    
    else:
        person_obj = get_object_or_404(Person, pk=id)
        form = PersonForm(model_to_dict(person_obj))

    context = {
        'form': form,
        'person_id': person_obj.id,
        'update_success': update_success
    }

    return render(request, 'pages/edit_person.html', context)