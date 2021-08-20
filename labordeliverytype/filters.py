import django_filters
from .models import Labordeliverytype


class LabordeliverytypeFilter(django_filters.FilterSet):                            # Labordeliverytypefilter used to filter based on name
    deliverytypename = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name
    class Meta:
        model = Labordeliverytype
        fields = ['deliverytypename']
