from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(models.Model):
    email = models.EmailField(primary_key=True)
    objects = models.Manager()

    def __str__(self):
        return self.email

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    image_url = models.URLField()
    recipe_url = models.URLField()
    calories = models.IntegerField(default=0)
    cuisine = models.CharField(max_length=120)
    diet = ArrayField(models.CharField(max_length=120),size=20)
    user = models.ManyToManyField(User, through='UserRecipe')
    objects = models.Manager()

    def __str__(self):
        return self.title


class UserRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    isFavorite = models.BooleanField(default = False)
    objects = models.Manager()
