from rest_framework import serializers
from .models import *
from acctcust.models import Acctcust
from configmaster.models import Configmaster
from configtable.models import Configtable
from labordeliverytype.models import Labordeliverytype
from labordelivery.models import Labordelivery
from product.models import Prodvendor, Category, Product
from order.models import Order, OrderItem


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'


class AcctcustSerializer(serializers.ModelSerializer):
	class Meta:
		model = Acctcust
		fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class ConfigmasterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Configmaster
		fields = '__all__'


class ConfigtableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Configtable
		fields = '__all__'


class LabordeliverytypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Labordeliverytype
		fields = '__all__'


class LabordeliverySerializer(serializers.ModelSerializer):
	class Meta:
		model = Labordelivery
		fields = '__all__'


class ProdVendorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Prodvendor
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = '__all__'

