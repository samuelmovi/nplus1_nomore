from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Expenses)
admin.site.register(models.Reports)
