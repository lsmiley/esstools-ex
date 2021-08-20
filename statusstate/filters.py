import django_filters
from .models import Statusstate


class StatusstateFilter(django_filters.FilterSet):                            # statusstatefilter used to filter based on name

    statusstatename = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Statusstate
        fields = ['statusstatename']
