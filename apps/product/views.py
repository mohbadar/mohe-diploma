from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCateory
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def get_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    return render(request, 'product/show.html', {
        "product":product
    })


def get_product_categories(request):

    product_categories = list(ProductCateory.objects.all().values())
    data = dict()
    data['product_categories'] = product_categories

    return JsonResponse(data)

def get_products_of_category(request, name):
	products = Product.objects.filter(category = ProductCateory.objects.filter(name=name).first())
	page = request.GET.get('page',6)

	paginator = Paginator(products,6)

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request, "product/products.html", {'products':products})


def get_all_products(request):
	products = Product.objects.all()
	page = request.GET.get('page',6)

	paginator = Paginator(products,6)

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request, "product/products.html", {'products':products})