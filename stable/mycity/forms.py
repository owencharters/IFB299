from django.forms import ModelForm
from .models import User
from .models import UserType
from django import forms
from .models import Document
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
        username = forms.CharField(max_length=30, required=True, help_text='Required.')
        user_firstname = forms.CharField(max_length=30, required=True, help_text='Required.')
        user_lastname = forms.CharField(max_length=30, required=True, help_text='Required.')
        user_type = forms.CharField(max_length=30, required=True, help_text='Required.')
        home_city = forms.CharField(max_length=30, required=True, help_text='Required.')
        class Meta:
                model = User
                fields = ['username', 'user_firstname', 'user_lastname', 'user_type', 'home_city', 'email', 'password']

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('description', 'document', )
