from django.contrib import admin

from .models import City
from .models import User
from .models import UserType

admin.site.register(City)
admin.site.register(User)
admin.site.register(UserType)
# Register your models here.
