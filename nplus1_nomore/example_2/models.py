from django.db import models

# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

