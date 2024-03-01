from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from product.models import Product


def index(request):  # correct
    return render(request, 'art/index.html', {})


def list_of_products(request):  # correct
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'art/product-list.html', context)


'''
    Check if the product is being favorited or unfavorited,
    If the user has already favorited the product, remove him/her
    If the user has not favorited the product yet, add him/her 
'''
@login_required
def favourites(request, product_id):
    product = get_object_or_404(Product, id=request.POST.get('fav'))
    if product.favorites.filter(id=request.user.id).exists():
        product.favorites.remove(request.user)
    else:
        product.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def product_favourite_list(request):
    user = request.user
    favorite_products = user.favorites.all()

    context = {
        'favorite_products': favorite_products
    }

    return render(request, 'products/product_favourite_list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    is_favorites = False
    if product.favorites.filter(id=request.user.id).exists():
        is_favorites = True
    context = {
        'product': product,
        'is_favorites': is_favorites
    }
    return render(request, 'art/product-detail.html', context)
