import django_filters
from .models import Acctcust


class AcctcustFilter(django_filters.FilterSet):                            # prodvendorfilter used to filter based on name
    acctname = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Acctcust
        fields = '__all__'
