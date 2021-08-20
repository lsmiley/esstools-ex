from django import forms
from product.models import Prodvendor


class ProdvendorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['vendorname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['vendorcodename'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['vendorcategory'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['numvendorproducts'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['vendornote'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['vendorweburl'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1phone'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2phone'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contractnum'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Prodvendor
        # fields = ['vendorname', 'vendorcategory', '', '', '', '', '', ]
        fields = '__all__'
