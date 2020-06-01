from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = (
            'user',
        )


def get_expense_form(user, data=None):
    form = ExpenseForm(data)
    form.fields['category'].queryset = user.categories.all()
    return form


@login_required()
def expense_create(request):
    if request.method == "POST":
        form = get_expense_form(request.user, request.POST)
        if form.is_valid():
            form.instance.user = request.user
            o = form.save()
            return redirect("expenses:list")
    else:
        form = get_expense_form(request.user)
    return render(request, "expenses/expense_form.html", {
        'form': form,
    })


@login_required()
def expense_list(request):
    q = request.GET.get('q')
    qs = request.user.expenses.order_by('-date')  # related_name on the Expense.user model field!
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, "expenses/expense_list.html", {
        'object_list': qs,
    })


@login_required()
def expense_detail(request, id: int):
    return render(request, "expenses/expense_detail.html", {
        'object': get_object_or_404(Expense, user=request.user, id=id),
    })
