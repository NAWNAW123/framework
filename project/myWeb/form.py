from django import forms
from .models import Customer




class Customersform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('Customer_name','Customer_address','Customer_phone')
