import django_filters
from product.models import Prodvendor


class ProdvendorFilter(django_filters.FilterSet):                            # prodvendorfilter used to filter based on name
    vendorname = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Prodvendor
        fields = ['vendorname', 'vendorcategory']
