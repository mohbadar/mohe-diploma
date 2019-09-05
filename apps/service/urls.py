from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.get_home, name="get_home"),
    path('categories/', views.get_service_categories, name="get_service_categories"),
	path(r'categories/<name>', views.get_services_of_category, name="get_services_of_category"),
    path(r'<slug>', views.get_service, name="get_service"),


	]
