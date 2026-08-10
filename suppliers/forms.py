from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
