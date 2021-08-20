from django import forms
from .models import Labordelivery


class LabordeliveryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['labordeliverytype'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['regionnumber'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['regions'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryoption'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['currencytype'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['defaultfte_year'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryctrcostfactor'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band2name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band2count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band2percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band3'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band3name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band3count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band3percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band4'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band4name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band4count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band4percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band5'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band5name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band5count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band5percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band6'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band6name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band6count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band6percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band7'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band7name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band7count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band7percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band8name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band8count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band8percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band9'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band9name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band9count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band9percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['band10'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band10name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['band10count'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['band10percentage'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})

        self.fields['bandstotalcount'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})
        self.fields['deliverytype'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryusedescription'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memodeliverynote1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryownerfirstname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryownerlastname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['deliveryownerfullname'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})
        self.fields['createby'].widget.attrs.update({'class': 'textinput form-control', 'readonly': 'readonly'})


    class Meta:
        model = Labordelivery
        fields = '__all__'
