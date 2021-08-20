import django_filters
from order.models import OrderItem


class OrderItemFilter(django_filters.FilterSet):                            # prodcategoryfilter used to filter based on name
    product = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', ]
