from django import forms
from product.models import Category


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['categoryname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['categorynote'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Category
        fields = '__all__'
