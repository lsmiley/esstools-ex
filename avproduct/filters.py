import django_filters
from .models import *


class ProdvendorFilter(django_filters.FilterSet):                            # prodvendorfilter used to filter based on name
    vendoryname = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Prodvendor
        fields = ['vendorname', 'vendorcategory']


class AvproductFilter(django_filters.FilterSet):                            # prodcategoryfilter used to filter based on name
    productname = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Avproduct
        fields = ['productname', 'prodvendor', 'prodcategory']


