from django.shortcuts import render
from datetime import datetime


def main(request):
    context = {'title': 'Главная',
               'year': datetime.now().year,
               }
    return render(request, 'main/main.html', context=context, )
