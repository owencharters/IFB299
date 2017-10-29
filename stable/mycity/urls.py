from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^$', views.index, name='index'),

]

if settings.DEBUG:
    (r'^MEDIA_URL', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
