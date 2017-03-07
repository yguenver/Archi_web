from django import forms
from django.contrib.auth import authenticate,login

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username ", max_length=30)
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)

class InscriptionForm(forms.Form):
    pseudo = forms.CharField(label="", initial="Pseudo", max_length=30)
    email = forms.EmailField(initial="E-mail", label="", widget=forms.EmailInput)
    password = forms.CharField(initial="Password", label="", widget=forms.PasswordInput)
    password.widget.render_value="a"
    passwordconf = forms.CharField(initial="Password", label="", widget=forms.PasswordInput)
    passwordconf.widget.render_value="a"
