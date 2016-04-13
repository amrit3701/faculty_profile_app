from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Profile(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    field = models.CharField(max_length=100)
    field_detail = models.CharField(max_length=1000)

    def __str__(self):
        return self.field
