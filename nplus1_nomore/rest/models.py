from django.db import models

# Create your models here.

class GrandParent(models.Model):
    name = models.CharField(max_length=25)


class Parent(models.Model):
    name = models.CharField(max_length=25)
    parent = models.ForeignKey(GrandParent, on_delete=models.SET_NULL, null=True, related_name="parents")


class Child(models.Model):
    name = models.CharField(max_length=25)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)
    grandparent = models.ForeignKey(GrandParent, on_delete=models.SET_NULL, null=True)
