from django import forms
from .models import *

class BeverageForm(forms.ModelForm):
   class Meta:
     model = Beverage
     fields = ['item', 'price', 'quantity', 'model_pic',]

class SnackForm(forms.ModelForm):
   class Meta:
     model = Snack
     fields = ['item', 'price', 'quantity', 'model_pic',]

class CanForm(forms.ModelForm):
   class Meta:
     model = Can
     fields = ['item', 'price', 'quantity', 'model_pic',]
