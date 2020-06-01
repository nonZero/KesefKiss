import random

import silly
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from expenses.models import Expense, Category


class Command(BaseCommand):
    help = "Create some silly expenses."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        # Expense.objects.all().delete()

        users = []
        for i in range(1, 6):
            username = f"user{i}"
            # get_or_create
            try:
                users.append(User.objects.create_user(username, password=username))
            except IntegrityError:
                users.append(User.objects.get(username=username))

        while Category.objects.count() < 10:
            Category.objects.create(name=silly.thing().title())

        categories = Category.objects.all()
        for i in range(n):
            Expense.objects.create(
                user=random.choice(users),
                category=random.choice(categories),
                title=silly.thing(),
                amount=random.randint(1, 10000) / 100,
                date=f"2020-05-{random.randint(1, 20):02}",
                description="\n".join([silly.sentence() for i in range(random.randint(1, 4))]),
            )
