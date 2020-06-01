from django.conf import settings
from django.core import validators
from django.db import models


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='categories')
    name = models.CharField(max_length=300)

    class Meta:
        unique_together = (
            ('user', 'name'),
        )
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='expenses')
    title = models.CharField(max_length=300)
    amount = models.DecimalField(decimal_places=2, max_digits=10, validators=[
        validators.MaxValueValidator(1_000_000),
        validators.MinValueValidator(0.50),
    ])
    date = models.DateField()
    description = models.TextField(blank=True)
    is_star = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def is_expensive(self):
        return self.amount > 50
