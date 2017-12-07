from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from ..models import Category, SubCategory, Brand, Item
from ..forms import ItemForm


@login_required
def product_list(request):
    products = Item.objects.filter(owner__pk=request.user.id)
    return render(request, 'bike/include/product_list.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect('/products/product_list/')
    else:
        form = ItemForm()
    return render(request, 'bike/include/product_form.html', {'form': form})


@login_required
def update_product(request, slug):
    product = get_object_or_404(Item, slug=slug, owner=request.user)
    
    form = ItemForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/products/product_list/')
    return render(request, 'bike/include/product_form.html', {'form': form})


@login_required
def delete_product(request, slug):
    product = get_object_or_404(Item, slug=slug)

    if request.method == 'POST':
        product.delete()
        return redirect(product_list)

    else:
        return render(request, 'bike/include/delete_product.html', {'product': product})
