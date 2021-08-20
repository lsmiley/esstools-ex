from django import forms
from .models import Configtable


class ConfigtableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['configmaster'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configcreatedate'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configmodifydate'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configdesc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configtype'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['confignotes'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['confignummber'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configtext'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['configlink'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['sizemodifier'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['vendormodifier'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['hoursmodifier'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['managementmodifier1stline'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['managementmodifier2ndline'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['riskfactor_low'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['riskfactor_med'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['riskfactor_high'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['othercost_education'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['othercost_travel'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['othercost_equipment'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['endpointrangemodifier1'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['endpointrangemodifier2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['endpointrangemodifier3'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['endpointrangemodifier4'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['endpointrangemodifier5'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['endpointrangemodifier6'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['rpt_biweeklymodifier'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['rpt_weeklymodifier'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['rpt_dailymodifier'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['rpt_custommodifier'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['defaultendpointfac'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fac_frachrs'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fac_adjwkstn'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fac_adjsvrs'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fac_adjips'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fac_svrcalc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac3'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac4'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac5'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac6'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac7'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac9'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac10'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac11'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['frm_componentfac12'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Configtable
        fields = '__all__'
