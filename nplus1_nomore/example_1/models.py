from django.db import models

# Create your models here.
class Reports(models.Model):
    name = models.CharField(max_length=255)
    submitted_date = models.DateTimeField(null=True, blank=False)

    @property
    def get_expense_total(self):
        total = 0
        for expense in self.expenses.all():
            total += expense.amount
        return total

class Expenses(models.Model):
    report = models.ForeignKey(Reports, related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
