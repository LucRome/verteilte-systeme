from django.forms import ModelForm, Form, ChoiceField, CharField, IntegerField, PasswordInput, HiddenInput
import string
import random
from .models import Person

class PersonFilterForm(Form):
    first_name = CharField(max_length=50, label='First Name', initial='', required=False)
    last_name = CharField(max_length=50, label='Last Name', initial='', required=False)

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthday']
