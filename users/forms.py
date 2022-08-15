from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from shop.bulma_mixin import BulmaMixin

class SignUpForm(BulmaMixin, UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your username')
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'input'}), label='Write your email')
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Create password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Repeat password')

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']




class SignInForm(BulmaMixin, AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Username')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Password')

    class Meta:
        model=User
        fields=['username', 'password']



