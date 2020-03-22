from .models import *
from collections import OrderedDict

def search_recipes_sorted(keywords):
    final_results_weighted = {}
    for word in keywords:
        results = search(word)
        for recipe in results.items():
            if recipe in final_results_weighted.items():
                final_results_weighted[recipe] += results[recipe]
            else:
                final_results_weighted[recipe] = results[recipe]
    return sort(final_results_weighted)


def search(word):
    ingredients = Ingredient.objects.get(name=r'.*{re.escape(word)}.*')
    cuisines = Cuisine.objects.get(name=r'.*{re.escape(word)}.*')
    diets = Diet.objects.get(name=r'.*{re.escape(word)}.*')
    recipes = Recipe.objects.get(title=r'.*{re.escape(word)}.*')

    results = {}

    #Increments weight of each recipe by a predetermined amount.
    #Recipe title is weighted higher, and so are multiple matches.
    if ingredients:
        ingredients_recipes = Recipe.objects.filter(ingredient=ingredients.name)
        for rec in ingredients_recipes:
            if rec in results:
                results[rec] += 1
            else:
                results[rec] = 1

    if cuisines:
        cuisine_recipes = Recipe.objects.filter(cuisine=cuisines.name)
        for rec in cuisine_recipes:
            if rec in results:
                results[rec] += 1
            else:
                results[rec] = 1

    if diets:
        diet_recipes = Recipe.objects.filter(diet=diets.name)
        for rec in diet_recipes:
            if rec in results:
                results[rec] += 1
            else:
                results[rec] = 1

    if recipes:
        for rec in recipes:
            if rec in results:
                results[rec] += 2
            else:
                results[rec] = 2

    return results


def sort(final_results):
    new_dict = OrderedDict(sorted(final_results.items(), key=lambda x: x[1], reverse=True))
    return list(new_dict.keys())


