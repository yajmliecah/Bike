from django import template
from ..models import Item, Brand, Edition, Category

register = template.Library()


@register.assignment_tag
def get_categories():
    return Category.objects.all()

@register.assignment_tag
def get_brands():
    return Brand.objects.all()

@register.assignment_tag
def get_editions():
    return Edition.objects.all()

@register.assignment_tag
def new():
    return Item.old()

@register.assignment_tag
def new():
    return Item.new()