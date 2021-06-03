from django import forms
from django.forms import ModelForm
from mobile.models import Product

class BrandForm(forms.Form):
    brand_name=forms.CharField()

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
