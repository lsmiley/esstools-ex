from rest_framework import serializers
from product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'



