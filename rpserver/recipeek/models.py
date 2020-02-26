from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    image_url = models.URLField()
    recipe_url = models.URLField()
    calories = models.IntegerField(default=0)
    cuisine = models.ManytoManyField(Cuisine)
    diet = models.ManytoManyField(Diet, through='RecipeIngredient')
    user = models.ManytoManyField(User, through='UserRecipe')

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    unit = models.CharField(max_length=36)
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)

class Ingredient(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name

class Diet(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return self.email

class UserRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
    isFavorite = models.BooleanField(default = false)
