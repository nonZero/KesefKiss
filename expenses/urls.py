from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path('kazabobo/', views.expense_list, name="list"),
    path('kukuriku67x/<int:id>/', views.expense_detail, name="detail"),
]
