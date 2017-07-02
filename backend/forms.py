from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from test import random

class SignUpForm(UserCreationForm):
    #server_id = forms.IntegerField()
    #server_id = random.randrange(0,10)
    company_name = forms.CharField(max_length=50)
    name = forms.CharField(max_length=40)
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2', 'company_name',)

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1',)

class IOForm(forms.Form):
    secret_key = forms.CharField(max_length=100)
    cipher_name = forms.CharField(max_length=100)
    public_key = forms.CharField(max_length=200)