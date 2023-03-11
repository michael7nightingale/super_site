from django.shortcuts import render, get_object_or_404
from .formulas.phy.TEMPLATES import template1
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import *
from datetime import datetime

from .models import *


phy = Phy.objects.all()
history = []


class CommonContextMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['year'] = datetime.now().year
        # ++ ++
        return context


class PhyMain(TemplateView, CommonContextMixin):
    template_name = "phy/main.html"
    model = Phy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Физика"
        context['categories'] = CategoryPhy.objects.all()
        context = dict(list(context.items()) + list(self.get_user_context().items()))
        return context


def phy_main(request):
    context = {'history': history, 'title': 'Физика'}
    return render(request, 'phy/main.html', context=context, )


class Mechanics(ListView):
    model = Formula
    template_name = "phy/mechanics.html"
    context_object_name = "formulas"

    def get_queryset(self):
        return Formula.objects.filter(cat=2), Formula.objects.filter(cat=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Механика"
        context['formulas_dinamics'], context['formulas_kimenatiks'] = self.get_queryset()
        return context


class Statics(ListView):
    model = Formula
    template_name = "phy/statics.html"
    context_object_name = "formulas"

    def get_queryset(self):
        return Formula.objects.filter(cat=5)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['formulas'][0].cat)
        return context


class CategoryPhysics(ListView, CommonContextMixin):
    template_name = "phy/category_physics.html"
    model = Formula
    context_object_name = "formulas"

    def get_queryset(self):
        return Formula.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = dict(list(context.items()) + list(self.get_user_context().items()))
        context['title'] = str(CategoryPhy.objects.get(slug=self.kwargs['cat_slug']).category_name)
        return context


def template_formula(request, formula_slug):
    linedb = get_object_or_404(Formula, slug=formula_slug)
    template_builder = getattr(template1, linedb.template_name)
    context = template_builder(request, linedb)
    context['category'] = get_object_or_404(CategoryPhy, category_name=linedb.cat)
    return render(request, 'phy/{}.html'.format(linedb.template_name), context=context)
