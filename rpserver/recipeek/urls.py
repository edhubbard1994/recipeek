from django.urls import path
from .views import RecipeView, hello_world


urlpatterns = [
    path('recipe/', RecipeView.as_view()),
    path('test/',hello_world)
]