from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class YourForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input', 'style': 'width: 300px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input'}))
