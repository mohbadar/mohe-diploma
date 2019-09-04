from django.urls import path, include
from . import views

urlpatterns = [
	path('categories/', views.get_post_categories, name="get_post_categories"),
	path(r'categories/<name>', views.get_posts_of_category, name="get_posts_of_category"),
    path(r'<slug>', views.get_post, name="get_post"),


]
