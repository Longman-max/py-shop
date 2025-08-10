from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# /products -> index
# (URL) Uniform Resource Locator(Address)
def index(request):
    # return HttpResponse('Hello there')
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('New products')


