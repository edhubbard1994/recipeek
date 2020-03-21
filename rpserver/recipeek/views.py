from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import *

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
    

@api_view(['POST'])
def import_recipes(request):
    return Response(status=200)
    
'''
class RecipeView(ModelViewSet):
  
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]
'''




