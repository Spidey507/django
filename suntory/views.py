from django.shortcuts import render, get_object_or_404
from .models import Product, Distillery

def product_list(request):
    products = Product.objects.all()
    return render(request, 'suntory/product_list.html', {'products': products})

def distillery_info(request):
    distillery = Distillery.objects.first()
    return render(request, 'suntory/distillery_info.html', {'distillery': distillery})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'suntory/product_details.html', {'product': product})