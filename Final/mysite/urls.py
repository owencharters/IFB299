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
    url(r'^$', views.login, name='login'),
    url(r'^mycity/', include('mycity.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.signup, name='register'),
    url(r'^mapupload/', views.model_form_upload, name='mapupload'),
    url(r'^login/$', auth_views.login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^administratorPage/', views.signup, name='administratorPage'),
    url(r'^login/', views.login, name='login'),
    url(r'^summary/(?P<button_id>[a-z]+?_?[a-z]+)/$', views.summary, name ='summary'),
	url(r'^summary/hotels/', views.summary, name ='summary1'),
    url(r'^profile/?', views.update_profile, name ='profile'),
    url(r'^signedUpSuccessfully/', views.signedUpSuccessfully, name ='signedUpSuccessfully'),
    url(r'^search/?$', views.search, name='search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
