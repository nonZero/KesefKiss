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
