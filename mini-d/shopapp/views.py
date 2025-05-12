from django.shortcuts import render

def index(request):
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
    }
    return render(request, 'index.html', context)

def cart(request):
    return render(request, 'cart.html')

def products(request):
    products_list = {
        1: {"name": "iPhone 14", "price": 1000, "description": "Мощный смартфон от Apple"},
        2: {"name": "Samsung Galaxy S23", "price": 950, "description": "Флагман от Samsung"},
        3: {"name": "Xiaomi 13", "price": 700, "description": "Бюджетный смартфон с топовыми характеристиками"}
    }
    return render(request, 'products.html', context={'products_list':products_list})

def product(request):
    product = {"name": "iPhone 14", "price": 1000, "description": "Мощный смартфон от Apple"}
    return render(request, 'product.html', context={'product':product})

def sell_phone(request):
    return render(request, 'sell_phone.html')

def add_to_cart(request):
    return render(request, 'index.html')

def remove_from_cart(request):
    return render(request, 'index.html')