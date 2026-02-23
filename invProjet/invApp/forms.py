from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Id du produit',
            'name': 'Nom',
            'ugs': 'Unité de gestion de stock',
            'price': 'Prix',
            'quantity': 'Quantité',
            'supplier': 'Fournisseur',
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g. Pull', 'class':'form-control'}),
            'ugs': forms.TextInput(attrs={'placeholder':'e.g. S560', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g. 14.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'e.g. Zara', 'class':'form-control'}),
        }