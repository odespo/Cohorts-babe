from __future__ import unicode_literals

from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    phone_number = PhoneNumberField(unique=True)

class Rating(models.Model):
    created_at = models.DateField(auto_now_add=True)
    person_rating = models.ForeignKey(Person)
    person_rated = models.ForeignKey(Person, related_name='person_rated') # TODO: make sure they can't be the same
    rating_list = models.TextField() # # JSON-serialized (text) version of ratings
