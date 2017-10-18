from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from mycity import views
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^mycity/', include('mycity.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register, name='register'),
    url(r'^mapupload/', views.model_form_upload, name='mapupload'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
]

