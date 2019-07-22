from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.filter(status=True)
    return render(request,'index.html', {"products" : products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {"product" : product})

def product_search(request):
    products = Product.objects.filter(name__contains = request.GET['product_search'])
    return render(request, 'index.html', {"products" : products})