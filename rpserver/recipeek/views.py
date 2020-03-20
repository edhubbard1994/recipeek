# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny
import requests
from .models import Recipe

#from .serializers import RecipeSerializer
from .search import search

import json
from bs4 import BeautifulSoup
# Create your views here.

#just a test view to see if this thing works

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
@api_view(['GET'])
def hello_world(request):
    global html_doc
    test_scrape = BeautifulSoup(html_doc,'html.parser')
    data_back = {
        'title' : str(test_scrape.title.extract()),
        'links' : [str(test_scrape.a.extract())]
        }
    return Response(data=data_back,status=200)

@api_view(['POST'])
def searchRequest(request):
    serialized = request.data
    search(serialized['keywords'])
    return Response({"Implement" : "At some point"})

'''
class RecipeView(ModelViewSet):
  
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]
'''

def get_recipes_api():
    # # url = 'https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=79fc7319904f45df944d73e6682a1163'
    url = 'https://api.edamam.com/search?q=chicken&app_id=84ccbee5&app_key=d8004719869b5827b1a5aa5b3256fdfc&from=0&to=3&calories=591-722&health=alcohol-free'
    r = requests.get(url)
    recipes = r.json()
    for i in range(len(recipes['hits'])):
        recipe = recipes['hits'][i]['recipe']
        curr_recipe = Recipe.objects.get(id=recipe['uri'])
        if not curr_recipe:
            r = Recipe(id=recipe['uri'], title=recipe['label'], image_url=recipe['image'], recipe_url=recipe['url'],
                       calories=recipe['calories'])
            r.save()
