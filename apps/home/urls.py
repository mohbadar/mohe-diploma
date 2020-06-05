from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_home, name="get_home"),
    path('newform.py', views.get_newform_view, name="mohe_newform")


	]
