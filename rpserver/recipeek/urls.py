from django.urls import path, include
from .views import  hello_world,searchRequest
from rest_framework.routers import DefaultRouter
#from .views import RecipeView

router = DefaultRouter()
#router.register(r'recipe', RecipeView)

urlpatterns = [
    #path('',include(router.urls)),
    path('test/', hello_world),
    path('search/', searchRequest),
]





