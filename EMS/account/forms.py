from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import fields


from .models import Leave, Profile, Holiday

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def save(self, commit=True):
        user= super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
        
class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'salary', 'phone_number', 'designation', 'bank_name', 'account_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateHolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['name', 'from_date', 'to_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'from_date' : forms.DateInput(attrs={'class': 'form-control'}),
            'to_date' : forms.DateInput(attrs={'class': 'form-control'}),
        }

class CreateLeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['from_date', 'to_date', 'reason']
        widgets = {
            'from_date' : forms.DateInput(attrs={'class': 'form-control'}),
            'to_date' : forms.DateInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
        }