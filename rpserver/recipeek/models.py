from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

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

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    image_url = models.URLField()
    recipe_url = models.URLField()
    calories = models.IntegerField(default=0)
    cuisine = models.ManyToManyField(Cuisine)
    diet = models.ManyToManyField(Diet, through='RecipeIngredient')
    user = models.ManyToManyField(User, through='UserRecipe')

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    unit = models.CharField(max_length=36)
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    diet = models.ForeignKey(Diet, on_delete=models.DO_NOTHING)

class UserRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    isFavorite = models.BooleanField(default = False)

