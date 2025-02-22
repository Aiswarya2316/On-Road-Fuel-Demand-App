from django import forms
from .models import Customer, Staf, AdminReg, Deliveryboy

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'password', 'location']
        widgets = {
            'password': forms.PasswordInput()
        }

class StafRegistrationForm(forms.ModelForm):
    class Meta:
        model = Staf
        fields = ['name', 'email', 'password', 'location']
        widgets = {
            'password': forms.PasswordInput()
        }

class AdminRegistrationForm(forms.ModelForm):
    class Meta:
        model = AdminReg
        fields = ['name', 'email', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class DeliveryBoyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Deliveryboy
        fields = ['name', 'email', 'password', 'location']
        widgets = {
            'password': forms.PasswordInput()
        }
