from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirm Password"}))
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
class CheckoutForm(forms.ModelForm):
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "city"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "address"}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "street"}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "state"}))
    pin_code = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "pin_code"}))
    landmark = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "landmark"}))
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['user']