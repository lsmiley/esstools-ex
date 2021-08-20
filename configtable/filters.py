import django_filters
from .models import Configtable


class ConfigtableFilter(django_filters.FilterSet):                            # Configtablenamefilter used to filter based on name
    Configname = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the Configtablename

    class Meta:
        model = Configtable
        fields = ['configname']
