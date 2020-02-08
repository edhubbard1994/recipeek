from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class RecipeModel(models.Model):
    name = models.CharField(max_length=120)
    meal = models.CharField(max_length=30, choices=(('breakfast','breakfast'),('lunch','lunch'),
        ('dinner','dinner'),('brunch','brunch'),('snack','snack'),('dessert','dessert'),('other','other')),default='other') 
    ingredients = ArrayField(models.CharField(max_length=120),size=30)
    instructions = ArrayField(models.CharField(max_length=500), null=True)
    tags = ArrayField(models.CharField(max_length=20),null=True)

    def __str__():
        return "Recipe"