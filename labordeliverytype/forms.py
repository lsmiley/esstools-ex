from django import forms
from .models import Labordeliverytype


class LabordeliverytypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['deliverytypename'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryusedescription'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memodeliverynote1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryownerfirstname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryownerlastname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryownerfullname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryowneremail'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['createby'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Labordeliverytype
        fields = '__all__'
