from django import forms
from django.contrib.auth import authenticate,login

class ConnexionForm(forms.Form):
    username = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    passwordconf = forms.CharField( label="", widget=forms.PasswordInput(attrs={'placeholder': 'Comfirm password'}))
