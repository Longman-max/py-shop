from django.db import models  # Importing the models module from Django

# Create your models here.

class Product(models.Model):  # Creating a Product model class that inherits from Django's Model class
    name = models.CharField(max_length=255)  # Defining a field for the product's name

    price = models.FloatField()  # Defining a field for the product's price

    stock = models.IntegerField()  # Defining a field for the product's stock quantity

    image_url = models.CharField(max_length=2083)  # Defining a field for the product's image URL


class Offer(models.Model):
    code = models.CharField(max_length=20)
    discount = models.IntegerField()
    description = models.CharField(max_length=2083)