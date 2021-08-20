import django_filters
from product.models import Product, Category


class ProductFilter(django_filters.FilterSet):                            # prodcategoryfilter used to filter based on name
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    prodvendor = django_filters.CharFilter(lookup_expr='icontains')# allows filtering without entering the full name

    class Meta:
        model = Product
        fields = ['title', 'category', 'prodvendor']

