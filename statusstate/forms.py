from django import forms
from .models import Statusstate


class StatusstateForm(forms.ModelForm):

    class Meta:
        model = Statusstate

        fields = '__all__'
