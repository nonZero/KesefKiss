from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path('', views.expense_list, name="list"),
    path('json/', views.expense_list_json, name="json"),
    path('create/', views.expense_create, name="create"),
    path('<int:id>/', views.expense_detail, name="detail"),
    path('<int:id>/star/', views.expense_star, name="star"),

    path('category/', views.CategoryListView.as_view(), name="category_list"),
    # path('category-better/', views.BetterCategoryListView.as_view(), name="category_list_better"),

]
