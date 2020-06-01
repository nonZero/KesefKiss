import random

import silly
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from expenses.models import Expense

CATS = "food car house utilities kids vacation etc fun investment pets lost".title().split()


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
                u = User.objects.create_user(username, password=username)
                for c in random.sample(CATS, random.randint(2, 5)):
                    u.categories.create(name=c)
                users.append(u)
            except IntegrityError:
                users.append(User.objects.get(username=username))

        for i in range(n):
            u = random.choice(users)
            Expense.objects.create(
                user=u,
                category=u.categories.order_by("?").first(),
                title=silly.thing(),
                amount=random.randint(1, 10000) / 100,
                date=f"2020-05-{random.randint(1, 20):02}",
                description="\n".join([silly.sentence() for i in range(random.randint(1, 4))]),
            )
