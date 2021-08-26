import auto_prefetch

from django.db import models

# Create your models here.


class Country(auto_prefetch.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(auto_prefetch.Model):

    name = models.CharField(max_length=100)
    country = auto_prefetch.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class Book(auto_prefetch.Model):

    title = models.CharField(max_length=100)
    author = auto_prefetch.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
