from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.get_home, name="get_home"),

    path('categories/', views.get_product_categories, name="get_product_categories"),
	path(r'categories/<name>', views.get_products_of_category, name="get_products_of_category"),
    path(r'<slug>', views.get_product, name="get_product"),



]
