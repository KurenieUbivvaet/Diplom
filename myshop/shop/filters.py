import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max price')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price']
