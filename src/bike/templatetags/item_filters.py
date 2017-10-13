from django import template
from ..models import Category, Item


register = template.Library()

def paginator(object):
    return {'object': object}
register.inclusion_tag('bike/include/_paginator.html')(paginator)

@register.assignment_tag
def new():
    return Item.objects.new()

@register.assignment_tag
def old():
    return Item.objects.old()