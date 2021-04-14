from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    if request.method == 'GET':
        try:
            query = request.GET.get('q')

            return redirect(search_result, query)
        except:
            messages.error(request, 'Пользователь не найден')
    return render(request, 'index.html')


def search_result(username):
    pass
