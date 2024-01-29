from django import forms
from .models import Avocat
from .models import Client
from .models import Contract
class AvocatForm(forms.ModelForm):
    class Meta:
        model = Avocat
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'data_start': forms.DateInput(attrs={'type': 'date'}),
            'data_sfarsit': forms.DateInput(attrs={'type': 'date'}),
        }