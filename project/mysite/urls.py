from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^mycity/', include('mycity.urls')),
    url(r'^admin/', admin.site.urls),
]

