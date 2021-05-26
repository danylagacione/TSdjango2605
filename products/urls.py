from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('list-products/', views.get_products),
    path('form/', views.post),
    path('list-categories/', views.get_categories),
    path('form-categories/', views.post_categories),
]
