from django import forms #forms import
from django.contrib.auth.forms import UserCreationForm #to create a user
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username = forms.CharField(label="Your Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Your Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
         Model=User
         fields=['username','email','password1','password2']
