from django import template
from ..models import Category, Item
from django.db.models import Count

register = template.Library()


@register.assignment_tag
def cars():
    return Item.objects.get_cars()

@register.assignment_tag
def motorcycles():
    return Item.objects.get_motorcycles()

@register.assignment_tag
def vehicles():
    return Item.objects.get_vehicles()

@register.assignment_tag
def new():
    return Item.objects.new()

@register.assignment_tag
def old():
    return Item.objects.old()
