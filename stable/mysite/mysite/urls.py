from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from mycity import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^mycity/', include('mycity.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register, name='register'),
    url(r'^mapupload/', views.model_form_upload, name='mapupload'),
    url(r'^login/$', auth_views.login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index.html'}, name='logout'),
    url(r'^administratorPage/', views.register, name='administratorPage'),

]
