from django.core import validators
from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=300)
    amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[
        validators.MaxValueValidator(1_000_000),
        validators.MinValueValidator(0.50),
    ])
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def is_expensive(self):
        return self.amount > 50
