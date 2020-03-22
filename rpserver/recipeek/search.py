from .models import *

def search(keywords):
    query_accumulator = []
    for word in keywords:
        results = lookup(word)
        if len(results) > 0:
            query_accumulator = query_accumulator + results
    return sort(query_accumulator)


def lookup(word):
    #TODO: database queries to find the word context

    ingredients = Ingredient.objects.get(name=r'.*{re.escape(word)}.*')
    cuisines = Cuisine.objects.get(name=r'.*{re.escape(word)}.*')
    diets = Diet.objects.get(name=r'.*{re.escape(word)}.*')
    recipes = Recipe.objects.get(title=r'.*{re.escape(word)}.*')

    results = set()

    if (ingredients):
        ingredients_recipes = Recipe.objects.filter(cuisine=cuisines.name)
        results.add(set(ingredients_recipes))
    if (cuisines):
        cuisine_recipes = Recipe.objects.filter(cuisine=cuisines.name)
        results.add(set(cuisine_recipes))
    if (diets):
        diet_recipes = Recipe.objects.filter(diet=diets.name)
        results.add(set(diet_recipes))
    if (recipes):
        results.add(recipes)
    #Remove duplicates
    return results

def sort(query_accumulator):
    #Sort here
    return query_accumulator
