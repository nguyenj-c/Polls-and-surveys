from django import forms
from django.forms import Form


class LoginForm(Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)


class RegisterForm(Form):
    email = forms.CharField(max_length=200, widget=forms.EmailField)
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

# def clean_username(self):
#       username = self.cleaned_data['email']
#      if not username.endswith("univ-amu.fr"):
#          self.add_error('email', "Vous devez faire parti de AMU.")
#     return


