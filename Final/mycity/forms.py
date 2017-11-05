from .models import Profile
from django import forms
from .models import Document
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    user_type = forms.CharField(max_length=20)
    home_city = forms.CharField(max_length=20)

    class Meta:
        model = Profile
        fields = ('user_type', 'home_city')


class SignupForm(UserCreationForm):
    user_type = forms.CharField(max_length=20, required=True)
    home_city = forms.CharField(max_length=20, required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'user_type', 'home_city')

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
