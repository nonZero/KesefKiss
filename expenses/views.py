from django.shortcuts import render


def expense_list(request):
    return render(request,
                  "expenses/expense_list.html", {
                      'word': 'xyzzy',
                      'nums': [23, 4, 5, 323, 2, 55],
                      'mylist': [
                          'milk',
                          'cookies',
                          'coffee',
                      ],
                  })
