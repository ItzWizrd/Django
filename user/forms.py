from django import forms

from .models import User


class Userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Username"}), label="Username")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email"}), label="Email")
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={"placeholder": "Enter Phone Number"}), label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Password"}), label="Password")

    class Meta:
        model = User
        fields = "__all__"
