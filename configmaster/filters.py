import django_filters
from .models import Configmaster


class ConfigmasterFilter(django_filters.FilterSet):                            # configmasternamefilter used to filter based on name
    configmastername = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the configmastername
    class Meta:
        model = Configmaster
        fields = ['configmastername']
