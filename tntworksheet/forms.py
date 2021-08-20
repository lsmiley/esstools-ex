from django import forms
from tntworksheet.models import Tntworksheet


class TntworksheetForm(forms.ModelForm):

    class Meta:
        model = Tntworksheet
        fields = '__all__'
