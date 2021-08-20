from django import forms
from .models import Acctcust


class AcctcustForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['acctname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['businesssec'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['regulatory'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['created'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['address1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['address2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['city'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['state'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['country'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1phone'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact1email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2phone'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['contact2email'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['wbsiteurl'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['createdby'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['modifydate'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Acctcust
        fields = '__all__'
