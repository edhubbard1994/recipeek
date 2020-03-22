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
    #Grab from API if needed

    ingredients = Ingredient.objects.get(name=r'.*{re.escape(word)}.*')
    cuisines = Cuisine.objects.get(name=r'.*{re.escape(word)}.*')
    diets = Diet.objects.get(name=r'.*{re.escape(word)}.*')
    recipes = Recipe.objects.get(title=r'.*{re.escape(word)}.*')

    results = []

    if (ingredients):
        results = results + list(ingredients)
    if (cuisines):
        results = results + list(cuisines)
    if (diets):
        results = results + list(diets)
    if (recipes):
        results = results + list(recipes)
    return results

def sort(query_accumulator):
    #Sort here
    return query_accumulator
