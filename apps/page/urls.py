from django.urls import path, include
from . import views

urlpatterns = [
    path('categories/', views.get_page_categories, name="get_page_categories"),
	path(r'categories/<name>', views.get_pages_of_category, name="get_pages_of_category"),
    path(r'<slug>', views.get_page, name="get_page"),


    # path('', views.get_home, name="get_home"),
]
