"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
"""
from django.urls import path, re_path, include
from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from apps.config import 

from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from django.contrib.auth.decorators import user_passes_test


login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = [
    # path('site-admin/', include('djadmin.urls')),
    path('', include('apps.home.urls')),
    path('generic.py/', include('apps.generic.urls')),
    path('admin/',  admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')), 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
