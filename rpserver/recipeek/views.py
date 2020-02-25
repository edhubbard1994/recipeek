from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import AllowAny


from .models import RecipeModel
from .serializers import RecipeSerializer
from .search import search

import json
# Create your views here.

#just a test view to see if this thing works
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def searchRequest(request):
    serialized = request.data
    search(serialized['keywords'])
    return Response({"Implement":"At some point"})
    

class RecipeView(ModelViewSet):
  
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]





