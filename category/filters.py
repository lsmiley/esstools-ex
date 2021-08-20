import django_filters
from product.models import Category


class CategoryFilter(django_filters.FilterSet):                            # prodcategoryfilter used to filter based on name
    title = django_filters.CharFilter(lookup_expr='icontains')
    categoryname = django_filters.CharFilter(lookup_expr='icontains')
    categorynote = django_filters.CharFilter(lookup_expr='icontains')# allows filtering without entering the full name

    class Meta:
        model = Category
        fields = ['title', 'categoryname', 'categorynote']
