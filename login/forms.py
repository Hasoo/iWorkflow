from django import forms

class LoginForm(forms.Form):
    user_id = forms.CharField(max_length=20)
    user_pass = forms.CharField(widget=forms.PasswordInput())