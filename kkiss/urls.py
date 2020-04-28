"""kkiss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("shalom!!!!")


def lucky(request, my_num):
    return HttpResponse(f"Your lucky number is {my_num}!!!!")


def do_the_add(request, a: int, b: int = 100):
    return HttpResponse(f"{a} + {b} = {a + b}")


def happy_birthday(request, name: str, age: int):
    return HttpResponse(f"{name} is {age} years old")


urlpatterns = [
    path('', home),
    path('lucky/<int:my_num>/', lucky),
    # Exercise #1:
    path('add/<int:a>/<int:b>/', do_the_add),

    # Exercise #2:
    # - Option 1: Use a default value in the function.
    path('add/<int:a>/', do_the_add),

    # - Option 2: Use kwargs.
    path('add-option-2/<int:a>/', do_the_add, kwargs={'b': 111}),

    path('birthday/<name>/<int:age>/', happy_birthday),
    path('birthday/<int:age>/<name>/', happy_birthday),

    path('admin/', admin.site.urls),
]
