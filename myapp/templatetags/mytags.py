#coding:utf-8
from django import template
# import re

register = template.Library()

@register.simple_tag
def nav_active(request, pattern):

    # if re.search(pattern, request.path):
    if request.path == pattern:
        return 'active'
    return ''