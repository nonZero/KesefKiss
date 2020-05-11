from django.core.exceptions import ValidationError
from django.test import TestCase

from expenses.models import Expense


class ExpensesTestCase(TestCase):
    def test_expense(self):
        o = Expense(
            title="Mercedes",
            amount=212_000,
            created_at=f"2020-02-23",
        )
        o.full_clean()
        o.save()
        self.assertTrue(o.is_expensive())

    def test_expense_too_big(self):
        o = Expense(
            title="Boeing 747",
            amount=212_000_000,
            created_at=f"2020-02-23",
        )
        self.assertRaises(ValidationError, o.full_clean)

    def test_expense_too_small(self):
        o = Expense(
            title="Bazooka",
            amount=0.02,
            created_at=f"2020-02-23",
        )
        self.assertRaises(ValidationError, o.full_clean)
