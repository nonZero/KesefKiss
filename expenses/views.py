from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from rest_framework import serializers

from expenses.models import Expense, Category


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = (
            'user',
            'is_star',
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
def expense_star(request, id: int):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    import time
    import random
    time.sleep(random.randint(1, 2))
    # TODO: reliable toggle :-)
    o = get_object_or_404(Expense, user=request.user, id=id)
    o.is_star = not o.is_star
    o.save()
    # return HttpResponse(f"star star-{'on' if o.is_star else 'off'}")
    return JsonResponse({
        'star': o.is_star,
    })


@login_required()
def expense_detail(request, id: int):
    return render(request, "expenses/expense_detail.html", {
        'object': get_object_or_404(Expense, user=request.user, id=id),
    })


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Expense
        fields = "__all__"


@login_required()
def expense_list_json(request):
    q = request.GET.get('q')
    qs = request.user.expenses.order_by('-date')  # related_name on the Expense.user model field!
    if q:
        qs = qs.filter(title__icontains=q)
    return JsonResponse({'items': ExpenseSerializer(qs, many=True).data})
    # return JsonResponse({'items': [ExpenseSerializer(o).data for o in qs]})
    # return JsonResponse({'items': [{
    #     'id': o.id,
    #     'amount': o.amount,
    #     'title': o.title,
    #     'date': o.date,
    #     'category': {
    #         'id': o.category.id,
    #         'name': o.category.name,
    #     },
    # } for o in qs]})


# @login_required()
# def category_list(request):
#     qs = request.user.categories.all()
#     return render(request, "expenses/category_list.html", {
#         'object_list': qs,
#     })

# class based views (CBV)


# class CategoryListView(View):
#     template_name = "my_template.html"
#     def get(self, request, *args, **kwargs):
#         return render(request, "my_template.html")
        # return render(request, self.template_name)

# class CategoryListView(TemplateView):
#     template_name = "my_template.html"
#     foo = 123
#
#     def bar(self):
#         return 10 * "!"
#
# class BetterCategoryListView(CategoryListView):
#     def bar(self):
#         return super().bar().center(50, "?")
#

class CategoryListView(LoginRequiredMixin, ListView):
    # queryset = Category.objects.order_by('-name')
    paginate_by = 5

    def get_queryset(self):
        return self.request.user.categories.all()

# class BetterCategoryListView(CategoryListView):
#     def get(self, request):
#         qs = self.get_queryset()
#         return JsonResponse({'items': self.get_queryset()})

