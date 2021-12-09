from django import forms
from order.models import OrderItem


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'
