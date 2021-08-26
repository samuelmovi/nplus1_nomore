from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)


class Person(models.Model):

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

