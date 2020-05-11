import random

import silly
from django.core.management.base import BaseCommand

from expenses.models import Expense


class Command(BaseCommand):
    help = "Create some silly expenses."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        Expense.objects.all().delete()
        for i in range(n):
            Expense.objects.create(
                title=silly.thing(),
                amount=random.randint(1, 10000) / 100,
                date=f"2020-05-{random.randint(1, 20):02}",
                description="\n".join([silly.sentence() for i in range(random.randint(1, 4))]),
            )
