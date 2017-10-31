from django.forms import ModelForm
from .models import Profile
from .models import UserType
from django import forms
from .models import Document
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('type_id', 'city_id')


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required.')
    password = forms.CharField(max_length=30, required=True, help_text='Required.')
  
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  'password', 'email')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
