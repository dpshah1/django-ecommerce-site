from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from products.models import *
from users.models import *

# Create your views here.
@login_required
def home(request):
    all_entries = Product.objects.all()
    current_user = request.user
    return render(request, 'pages/product_home.html', {'all_entries' : all_entries, 'user' : current_user})

@login_required
def product_page(request, product_id):
    prod = Product.objects.get(pk = product_id)
    return render(request, 'pages/product_page.html', {'product' : prod})

@login_required
def puchase_item(request, product_id):
    prod = Product.objects.get(pk = product_id)
    current_user = Customer.objects.get(user = request.user)
    print(prod)
    print(current_user)
    p = Purchase(product = prod, purchaser = current_user)
    p.save()
    return render(request, 'pages/product_page.html', {'product' : prod})