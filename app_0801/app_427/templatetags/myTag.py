from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register 名字是固定的,無法改變


@register.filter
def kenson_sum(x, y):
    return x + y

@register.simple_tag
def simple_kenson(x,y,z):
    return x*y+z
