from django import template
from ..models import Item

register = template.Library()


@register.assignment_tag
def get_cars():
    return Item.objects.filter(category__name__icontains='Car')

@register.assignment_tag
def get_motorcycles():
    return Item.objects.filter(category__name__icontains='Motorcycle')

@register.assignment_tag
def get_vehicles():
    return Item.objects.filter(category__name__icontains='Vehicles')

@register.assignment_tag
def new():
    return Item.old()

@register.assignment_tag
def new():
    return Item.new()
