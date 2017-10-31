from django.forms import ModelForm
from .models import User
from .models import Profile
from .models import UserType
from django import forms
from .models import Document
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):
        username = forms.CharField(max_length=30, required=True, help_text='Required.')
        password = forms.CharField(max_length=30, required=True, help_text='Required.')
        class Meta:
                model = User
                fields = ['username', 'firstname', 'lastname', 'password', 'home_city', 'email']

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('description', 'document', )
		

class SignupForm(ModelForm):
        username = forms.CharField(max_length=30, required=True, help_text='Required.')
        password = forms.CharField(max_length=30, required=True, help_text='Required.')
        class Meta:
                model = User
                fields = ['username', 'firstname', 'lastname', 'password', 'user_type', 'home_city', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('type_id', 'city_id')
