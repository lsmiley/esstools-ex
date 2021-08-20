from django import forms
from .models import *


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


class AvproductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)

        self.fields['prodcategory'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['prodvendor'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['productname'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['productdesc'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['producttype'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['producttypefamily'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['productnote'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['productnote'].widget.attrs.update({'class': 'media form-control'})
        self.fields['productcomplexitybase'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['productcomplexityfac'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['numcomponent'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['primarycomp'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['primarycompdesc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['primarycomplexity'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['totalcomplexity'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component1desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac1'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent1note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent1technote'].widget.attrs.update({'class': 'textinput form-control'})


        self.fields['component2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component2desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac2'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent2note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent2technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component3'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component3desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs3'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac3'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent3note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent3technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component4'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component4desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs4'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac4'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent4note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent4technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component5'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component5desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs5'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac5'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent5note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent5technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component6'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component6desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs6'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac6'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent6note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent6technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component7'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component7desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs7'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac7'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent7note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent7technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component8desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent8note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent8technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component9'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component9desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs9'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac9'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent9note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent9technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component10'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component10desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs10'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac10'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent10note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent10technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component11'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component11desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs11'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac11'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent11note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent11technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component12'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component12desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs12'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac12'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent12note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent12technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component13'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component13desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs13'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac13'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent13note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent13technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component14'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component14desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs14'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac14'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent14note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent14technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['component15'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['component15desc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityhrs15'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['componentcomplexityfac15'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent15note'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memocomponent15technote'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['componentcomplexityhrstotal'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['numcomponents'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['memoproductnote'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['endpoint_ip'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['prodimage'].widget.attrs.update({'class': 'file form-control'})



    class Meta:
        model = Avproduct
        # fields = ['productname', 'prodcategory', 'prodvendor']
        fields = '__all__'


class ProdcategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['categoryname'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['categorynote'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Prodcategory
        fields = '__all__'
