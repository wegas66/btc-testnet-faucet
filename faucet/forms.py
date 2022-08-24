from django import forms
from .models import Address, Transaction


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address']
