from django import forms
from .models import Product, Category
from suppliers.models import Supplier

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)
    category = forms.ModelChoiceField( queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=3,widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001'}))
    stock_quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    reorder_level = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    supplier_details = forms.ModelMultipleChoiceField(queryset=Supplier.objects.all(),widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = '__all__'