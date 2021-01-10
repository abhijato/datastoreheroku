from django import forms

class loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'unm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'pwd'}))
