from django.forms import ModelForm
from .models import User
from .models import UserType

class UserForm(ModelForm):
        class Meta:
                model = User
                fields = ['username', 'user_firstname', 'user_lastname', 'user_type', 'home_city', 'email', 'password']
