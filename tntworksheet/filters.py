import django_filters
from tntworksheet.models import Tntworksheet


class TntworksheetFilter(django_filters.FilterSet):                            # prodvendorfilter used to filter based on name
    tntdescription = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Tntworksheet
        fields = ['tntdescription']
