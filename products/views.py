from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'index.html')

def get_products(request):
    return render (request, 'products.html')

def post(request):
    return render (request, 'form.html')

def get_categories(request):
    return render (request, 'categories.html')    

def post_categories(request):
    return render (request, 'form-categories.html')
