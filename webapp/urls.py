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

urlpatterns = [
    # path('site-admin/', include('djadmin.urls')),
    path('', include('apps.home.urls')),
    # path('products/', include('apps.product.urls')),
    # path('services/', include('apps.service.urls')),
    # path('posts/', include('apps.post.urls')),
    # path('projects/', include('apps.project.urls')),
    # path('contents/', include('apps.page.urls')),
    path('admin/',  admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
