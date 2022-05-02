from django.forms import ModelForm, Form, ChoiceField, CharField, IntegerField, PasswordInput, HiddenInput
import string
import random

class PersonFilterForm(Form):
    first_name = CharField(max_length=50, label='First Name', initial='', required=False)
    last_name = CharField(max_length=50, label='Last Name', initial='', required=False)
