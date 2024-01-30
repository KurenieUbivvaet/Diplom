from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    search_query = request.GET.get('search', '')
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    #фильтрация по поиску или по категории
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if search_query:
        products = products.filter(name__icontains=search_query)

    #разбиение на страницы
    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'page_obj': page_obj})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
