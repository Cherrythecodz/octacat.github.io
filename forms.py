from django import forms
from .orders import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['sender_name', 'recipient_name', 'package_details', 'delivery_preferences']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['Firstname', 'Lastname', 'email', 'password1', 'password2']
        
