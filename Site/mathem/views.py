from django.shortcuts import render
from .formulas.mathem.equations.equation_line import *
import django.utils.datastructures as django_data
from datetime import datetime
import functools


history = []


def emptyData(title, template):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except django_data.MultiValueDictKeyError:
                request = args[0]
                return render(request, template, context={'title': title,
                                                          'year': datetime.now().year,                                                                        'history': history})
        return wrapper
    return decorator


def mathem_main(request):
    context = {'title': 'Математика', 'history': history}
    return render(request, 'mathem/main1.html', context=context)


def form_history(result):
    if result:
        if len(history) < 8:
            history.insert(0, result)
        else:
            del history[-1]
            history.insert(0, result)
    return history


@emptyData(title='Линейные уравнения', template='mathem/equation_line1.html')
def equation_line(request):
    result = equation(request.POST['equation'], request.POST['root'], request.POST['nums_comma'])
    form_history(result)
    context = {'title': 'Линейные уравнения', 'self': 'equation_line', 'history': history, 'result': result}
    return render(request, 'mathem/equation_line1.html', context=context)


@emptyData(title='Математика', template='mathem/main1.html')
def mathem_mainDecorated(request):
    context = {'title': 'Математика', 'history': history}
    return render(request, 'mathem/main1.html', context=context)


