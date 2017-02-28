from ..models import Item, Brand, Edition
from django.shortcuts import render_to_response, render


def search(request):
    try:
        q = request.GET['q']
        items = Item.objects.filter(name__search=q) | \
                Item.objects.filter(category__search=q) | \
                Item.objects.filter(brand__search=q)
        return render(request, 'results.html', {'items': items, 'q': q})
    except KeyError:
        return render(request, 'results.html')