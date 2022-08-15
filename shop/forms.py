from django import forms
from .models import *
from .bulma_mixin import BulmaMixin



class OrderForm(BulmaMixin, forms.Form):
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your address')
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your phone')

    class Meta:
        model=Order
        fileds=['address', 'phone']