from django import template
from django.template.defaultfilters import stringfilter
import os


register = template.Library()


@register.filter()
@stringfilter
def basename(value):
    return os.path.basename(value)

@register.filter()
@stringfilter
def sizeof(value):
    num = int(value)
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f %sB" % (num, unit)
        num /= 1024.0
    return "%.1f %sB" % (num, 'Yi')
