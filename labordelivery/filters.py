import django_filters
from .models import Labordelivery


class LabordeliveryFilter(django_filters.FilterSet):                            # prodcategoryfilter used to filter based on name
    regions = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Labordelivery
        fields = ['regions']
