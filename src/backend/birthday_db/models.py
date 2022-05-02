from django.db import models

# Create your models here.
class Person(models.Model):
    birthday = models.DateField()
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)