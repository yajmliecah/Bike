from django import template
from ..models import Category
from django.db.models import Count

register = template.Library()


@register.assignment_tag
def cars():
    return Category.objects.distinct().filter(name__icontains='Cars')

@register.assignment_tag
def motorcycles():
    return Category.objects.distinct().filter(name__icontains='Motorcycles').annotate(toys_num=Count('brand'))

@register.assignment_tag
def vehicles():
    return Category.objects.filter(name__icontains='Vehicles')

@register.assignment_tag
def new():
    return Item.old()

@register.assignment_tag
def new():
    return Item.new()
