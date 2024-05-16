from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductSpecifications
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.db.models import Min, Max


def product_list(request, category_slug=None):
    search_query = request.GET.get('search', '')

    # получаем категорию
    category = None
    categories = Category.objects.all()

    # Получение всех продуктов
    products = Product.objects.filter(available=True)

    # Применение фильтрации по категории, если выбрана
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Применение фильтрации по поисковому запросу
    if search_query:
        products = products.filter(name__icontains=search_query)

    product_filter = ProductFilter(request.GET, queryset=products)
    products = product_filter.qs
    min_price_from_db = Product.objects.aggregate(Min('price'))['price__min']
    max_price_from_db = Product.objects.aggregate(Max('price'))['price__max']

    # Разбиение на страницы
    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'page_obj': page_obj,
        'product_filter': product_filter,
        'min_price_from_db': min_price_from_db,
        'max_price_from_db': max_price_from_db,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    product_spec = ProductSpecifications.objects.filter(products=product)
    cart_product_form = CartAddProductForm()
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'product_spec': product_spec,
                                                        'related_products': related_products,
                                                        'cart_product_form': cart_product_form})
