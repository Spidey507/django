from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Distillery, Review

def product_list(request):
    products = Product.objects.all()
    return render(request, 'suntory/product_list.html', {'products': products})

def distillery_info(request):
    distillery = Distillery.objects.first()
    return render(request, 'suntory/distillery_info.html', {'distillery': distillery})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all()
    return render(request, 'suntory/product_details.html', {'product': product, 'reviews': reviews})

def review_form(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        # Process the form data and save the review
        title = request.POST.get('title')
        body = request.POST.get('body')

        # Create a new Review object associated with the product and save it to the database
        review = Review(title=title, body=body, product=product)
        review.save()

        # Redirect the user to the product_details page
        return redirect('suntory:product_details', id=id)

    return render(request, 'suntory/review_form.html', {'product': product})