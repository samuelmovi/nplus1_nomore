from django.db import models


class Expenses(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)


# Create your models here.
class Reports(models.Model):
    name = models.CharField(max_length=255)
    expenses = models.ManyToManyField(Expenses,)

    @property
    def get_expense_total(self):
        total = 0
        for expense in self.expenses.all():
            total += expense.amount
        return total
