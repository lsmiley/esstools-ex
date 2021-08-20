from django import forms
from .models import Configmaster

class ConfigmasterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['created'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configmastermodifydate'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configmastername'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configmasterdesc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configmasternotes'].widget.attrs.update({'class': 'textinput form-control'})


    class Meta:
        model = Configmaster
        fields = '__all__'
