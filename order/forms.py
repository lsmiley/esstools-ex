from django import forms

import labordelivery
from .models import Order, OrderItem




class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderCreateForm(BaseForm, forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['date', 'title']


class OrderEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['labordelivery'].queryset = labordelivery.objects.none()


class OrderItemEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'
