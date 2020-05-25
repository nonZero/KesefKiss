from django.core import validators
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='expenses')  # 1-to-many
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
