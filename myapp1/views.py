from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def product_table(request):
    products = Product.objects.all()
    return render(request, 'myapp1/product_table.html', {'products': products})

def demo(request):
    return HttpResponse('HELLO')


def log(request):
    return render(request,'myapp1/log.html')

def reg(request):
    return render(request,'myapp1/reg.html')

def bootstrap(request):
    return render(request,'myapp1/Bootstrap.html')

def index(request):
    return render(request,'myapp1/index.html')