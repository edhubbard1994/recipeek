from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import *
from fractions import Fraction
from .search import *
import logging

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
    logging.warning(serialized['keywords'])
    recipes = search_recipes_sorted(serialized['keywords'])
    # recipes = search(request.data['keywords'])
    # temp = {'chicken'}
    # recipes = search_recipes_sorted(temp)

    acc =[]
    for recipe in recipes:
        json = {
            'name': recipe.title,
            'url': recipe.recipe_url,
            'calories': recipe.calories
        }
        acc.append(json)
    return Response(data=acc,status=200)
    

@api_view(['POST'])
def import_recipes(request):
    print(len(request.data))
    recipe_names = [recipe['title'] for recipe in request.data]
    querys = Recipe.objects.filter(title__in=recipe_names)
    existing_names = set({})
    for query in querys:
        if query.title in recipe_names:
            existing_names.add(query.title)
    print('existing:')
    print(existing_names)
    unique_requests = [recipe for recipe in request.data if recipe['title'] not in existing_names ]
    print("uniques:")
    print(len(unique_requests))
    arr = unique_requests
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
                i['ingredient'][:199] 
            )
            ing.save()
    return Response(status=200)

    




