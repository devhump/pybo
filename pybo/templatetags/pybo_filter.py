# mysite/pybo/templatetags/pybo_filter.py

from django import template
import markdown # 추가
from django.utils.safestring import mark_safe # 추가

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):

    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))