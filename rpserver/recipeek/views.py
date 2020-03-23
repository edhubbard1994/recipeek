from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import *
from fractions import Fraction

#from .serializers import RecipeSerializer
from .search import search

import json
from bs4 import BeautifulSoup
# Create your views here.

#just a test view to see if this thing works


@api_view(['GET'])
def hello_world(request):
    recipes = Recipe.objects.all()
    acc =[]
    for recipe in recipes:
        json = {
            'name': recipe.title,
            'url': recipe.recipe_url,
            'calories':recipe.calories
        }
        acc.append(json)
        
    return Response(data=acc,status=200)

@api_view(['POST'])
def searchRequest(request):
    serialized = request.data
    search(serialized['keywords'])
    return Response({"Implement" : "At some point"})
    

@api_view(['POST'])
def import_recipes(request):
    print(request.data)
    recipe_names = [recipe['title'] for recipe in request.data]
    query = Recipe.objects.filter(title__in=recipe_names)
    arr = request.data
    for recipe in arr:
        cuisine = Cuisine.objects.get_or_create(name=recipe['cuisine'])
        diet = Diet.objects.get_or_create(name='unknown')
        image_url = 'unknown'
        calories = 0
        try:
            calories = recipe['calories']
        except:
            pass
        try:
            image_url = recipe['image_url']
        except:
            pass
        try:
            diet = Diet.objects.get_or_create(name=recipe['diet'])
        except:
            diet = Diet.objects.get_or_create(name='unknown')

        r = Recipe(
            title=recipe['title'],
            image_url=image_url,
            recipe_url=recipe['recipe_url'],
            calories=calories,
            #cuisine=cuisine
            )
        r.save()
        #r.diet.add(diet)
        #r.calories.set(calories)
        #r.cuisine.set(cuisine)
        for i in recipe['ingredients']:
            amount = 1.0
            if type(i['amount']) == str:
                try:
                    amount = float(Fraction(i['amount']))
                except:
                    amount = 1.0
            else:
                try:
                    amount = float(i['amount'])
                except:
                    amount = 1.0
            ing = Ingredient(
                i['ingredient']
            )
            ing.save()

    print(list(query))
    return Response(status=200)
    
'''
class RecipeView(ModelViewSet):
  
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]
'''




