from django import forms
from matplotlib.pyplot import title

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                "title", 
                "price", 
                "summary", 
                "discription", 
                "featured", 
        ]
    
class RawProductForm(forms.Form):
    title = forms.CharField()
    price = forms.DecimalField()
    summary = forms.CharField()
    discription = forms.CharField()
    featured = forms.BooleanField()
