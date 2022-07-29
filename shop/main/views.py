from django.shortcuts import render
from .models import Product
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {"products" : products})


def profile(request):
    return render(request, 'main/profile.html', {})


