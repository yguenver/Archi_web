from django import forms
from django.contrib.auth import authenticate,login

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label="Username ", initial="", max_length=30, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(label="E-mail ", initial="", widget=forms.EmailInput(attrs={'placeholder':'E-mail'}))
    password = forms.CharField(label="Password ", initial="", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    passwordconf = forms.CharField(label="Confirm ", initial="", widget=forms.PasswordInput(attrs={'placeholder':'Confirm'}))

