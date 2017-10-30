from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from mycity import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mycity/', include('mycity.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register, name='register'),
    url(r'^mapupload/', views.model_form_upload, name='mapupload'),
    url(r'^login/$', auth_views.login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index.html'}, name='logout'),
    url(r'^administratorPage/', views.register, name='administratorPage'),
    url(r'^login/', views.login, name='login'),
    url(r'^summary/?', views.summary, name ='summary'),
    url(r'^profile/?', views.profile, name ='profile'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
