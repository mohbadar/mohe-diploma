from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_home, name="get_home"),
    path('newform.py', views.get_newform_view, name="eform_newform"),
    path(r'centers.py', views.get_centers_of_tenant, name="get_centers_of_tenant"),


	]
