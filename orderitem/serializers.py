from rest_framework import serializers
from order.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
