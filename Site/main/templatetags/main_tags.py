from django import template
from main.models import *

register = template.Library()


@register.simple_tag(name='getdata')
def main_test_tag():
    return Main.objects.all()
