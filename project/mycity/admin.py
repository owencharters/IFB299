from django.contrib import admin

from mycity.models import User
from mycity.models import UserType
from mycity.models import Weather
from mycity.models import Cities
from mycity.models import Libraries
from mycity.models import Colleges
from mycity.models import Departments
from mycity.models import Industries
from mycity.models import IndustryType
from mycity.models import Parks
from mycity.models import Hotels
from mycity.models import Museums
from mycity.models import Zoos
from mycity.models import Malls
from mycity.models import Restaurants



admin.site.register(User)
admin.site.register(UserType)
admin.site.register(Weather)
admin.site.register(Cities)
admin.site.register(Libraries)
admin.site.register(Colleges)
admin.site.register(Departments)
admin.site.register(Industries)
admin.site.register(IndustryType)
admin.site.register(Parks)
admin.site.register(Hotels)
admin.site.register(Museums)
admin.site.register(Zoos)
admin.site.register(Malls)
admin.site.register(Restaurants)
