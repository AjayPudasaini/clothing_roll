from django.shortcuts import render
from .models import Category, Product, Brand
# Create your views here.
def Index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brand = Brand.objects.all()
    contex = {"product":products, "categories":categories, "brand":brand}
    return render(request, 'clothing_roll/index.html', contex)


def ListAllProducts(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    contex = {"product":products, "categories":categories}
    return render(request, 'clothing_roll/list_all_products.html', contex)


def ProductDetail(request, slug):
    product = Product.objects.get(slug=slug)
    # print("hello", product.category)
    similar_products = Product.objects.filter(category=1)
    print( 'hello',similar_products)
    contex = {'product':product}
    return render(request, 'clothing_roll/product_detail.html', contex)