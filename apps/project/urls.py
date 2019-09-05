from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.get_home, name="get_home"),

    path('categories/', views.get_project_categories, name="get_project_categories"),
	path(r'categories/<name>', views.get_projects_of_category, name="get_projects_of_category"),
    path(r'<slug>', views.get_project, name="get_project"),



]
