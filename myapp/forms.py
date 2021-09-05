from django import forms
from django.contrib.auth.models import User
from .models import GroceryUpload
from django.forms import ModelForm


class GroceryForm(forms.ModelForm):
 class Meta:
  model = GroceryUpload
  fields = ['itemname','itemquantity', 'status', 'date']
  labels = {'itemname':'Item Name','itemquantity':'Item Quantity', 'status': 'Status', 'date':'Date'}
  widgets = {
   'itemname':forms.TextInput(attrs={'class':'form-control'}),
   'itemquantity':forms.TextInput(attrs={'class':'form-control'}),
   'date':forms.DateInput(attrs={'class':'form-control'}),
   
  }
