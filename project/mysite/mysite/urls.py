from django.conf.urls import include, url
from django.contrib import admin
from index import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'Templates/index.html'}, name='login'),
    url(r'^mycity/', include('mycity.urls')),
    url(r'^admin/', admin.site.urls),
]

