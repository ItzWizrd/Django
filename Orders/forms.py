from django import forms
from .models import Order, Product

class OrdersForm(forms.ModelForm):
    customer = forms.Select(attrs={'class': 'form-control'})
    order_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date", 'class': 'form-control'}))
    status = forms.ChoiceField(choices=Order.OrderStatus.choices, widget=forms.Select(attrs={'class': 'form-control'}))
    order_details = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Order
        fields = '__all__'