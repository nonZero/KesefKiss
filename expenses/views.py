from django.shortcuts import render

from expenses.models import Expense


def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
        'foo': '<b>shalom!</b> <i>bye!</i>',
    })


def expense_detail(request, id: int):
    return render(request, "expenses/expense_detail.html", {
        'object': Expense.objects.get(id=id),
    })
