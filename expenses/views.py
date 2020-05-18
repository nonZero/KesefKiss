from django.shortcuts import render

from expenses.models import Expense


def expense_list(request):
    request.session['foo'] = 12345
    request.session['bar'] = 'shalom shalom'
    resp = render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
        'foo': '<b>shalom!</b> <i>bye!</i>',
    })
    return resp


def expense_detail(request, id: int):
    print(request.session.items())
    return render(request, "expenses/expense_detail.html", {
        'object': Expense.objects.get(id=id),
    })
