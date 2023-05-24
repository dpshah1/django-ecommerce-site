from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    all_entries = Product.objects.all()
    return render(request, 'pages/product_home.html', {'all_entries' : all_entries})

@login_required
def product_page(request, product_id):
    prod = Product.objects.get(pk = product_id)
    return render(request, 'pages/product_page.html', {'product' : prod})
