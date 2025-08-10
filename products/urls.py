from django.urls import path  # Importing the path function from Django's urls module
from . import views  # Importing views module from the current directory

# URL patterns for the 'products' app

# Mapping the root URL '/products' to the index view function
# /products -> path('', views.index)
# This URL will trigger the index view function defined in views.py
# It represents the main page of the products app
urlpatterns = [
    path('', views.index),  # Root URL pattern
    # Mapping the URL '/products/new' to the new view function
    # /products/new -> path('new', views.new)
    # This URL will trigger the new view function defined in views.py
    # It represents a page for adding new products
    path('new', views.new),  # New product creation URL pattern
]
