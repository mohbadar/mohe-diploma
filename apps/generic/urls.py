from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/savenew', views.contact_savenew, name="contact_savenew")


	]
