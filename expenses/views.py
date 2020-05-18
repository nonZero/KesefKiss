from django import forms
from django.shortcuts import render, redirect

from expenses.models import Expense


# class ExpenseForm(forms.Form):
#     title = forms.CharField()
#     amount = forms.DecimalField(decimal_places=2, max_digits=10)
#     are_you_sure = forms.BooleanField()
#     type_of_pizza = forms.ChoiceField(choices=[
#         ('O', 'Olive'),
#         ('M', 'Mushroom'),
#         ('X', 'Everything'),
#     ])

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"


def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # assert False, form.cleaned_data
            o = form.save()
            return redirect("expenses:list")
        # else:
        #     assert False, form.errors
    else:
        form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {
        'form': form,
    })

def expense_list(request):
    return render(request, "expenses/expense_list.html", {
        'object_list': Expense.objects.all(),
    })


def expense_detail(request, id: int):
    return render(request, "expenses/expense_detail.html", {
        'object': Expense.objects.get(id=id),
    })
