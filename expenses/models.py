from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=300)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateField()
