from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

class RecipeView(APIView):
    def get(self, request, pk, format=None):
        return Response({
            "hello":"World"
        })
    
    def get_queryset(self):
        return Response([]) #super().get_queryset()
    



@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})