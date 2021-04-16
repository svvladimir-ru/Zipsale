from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views import View
from .utils import parser


def index(request):
    """Главная страница с поиском"""
    return render(request, 'index.html')


class SearchResultsView(View):
    """Отдает результат поиска"""
    template_name = 'search_results.html'

    def get(self, request):
        try:
            username = self.request.GET.get('q')
            context = parser(username)
            return render(request, 'search_result.html', {'context': context})
        except:
            messages.error(request, 'Пользователь не найден')
