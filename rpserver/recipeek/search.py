from .models import *
from collections import OrderedDict
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
import logging

def search_recipes_sorted(keywords):
    final_results_weighted = {}
    for word in keywords:
        results = search(word)
        for recipe in results:
            if recipe in final_results_weighted.keys():
                final_results_weighted[recipe] += results[recipe]
            else:
                final_results_weighted[recipe] = results[recipe]
    return sort(final_results_weighted)


def search(word):
    # ingredients = Ingredient.objects.filter(name__icontains=word)
    # cuisines = Cuisine.objects.filter(name__icontains=word)
    # diets = Diet.objects.filter(name__icontains=word)
    # recipes = Recipe.objects.filter(title__icontains=word)
    # logging.warning(recipes)

    results = {}

    # recipes = Recipe.objects.annotate(
    #     search=SearchVector('title'
    #                         # , 'ingredient__name', 'diet__name', 'cuisine__name'),
    #                         ),
    # ).filter(search=word)

    vector = SearchVector('title')
    query = SearchQuery(word)
    recipes = Recipe.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')

    logging.warning(recipes)

    for recipe in recipes:
        results[recipe] = 1

    #Increments weight of each recipe by a predetermined amount.
    #Recipe title is weighted higher, and so are multiple matches.
    # if ingredients:
    #     logging.warning(ingredients[0].name)
    #     ingredients_recipes = Recipe.objects.filter(ingredient__name=ingredients[0].name)
    #     for rec in ingredients_recipes:
    #         if rec in results:
    #             results[rec] += 1
    #         else:
    #             results[rec] = 1
    #
    # if cuisines:
    #     cuisine_recipes = Recipe.objects.filter(cuisine__name=cuisines[0].name)
    #     for rec in cuisine_recipes:
    #         if rec in results:
    #             results[rec] += 1
    #         else:
    #             results[rec] = 1
    #
    # if diets:
    #     diet_recipes = Recipe.objects.filter(diet__name=diets[0].name)
    #     for rec in diet_recipes:
    #         if rec in results:
    #             results[rec] += 1
    #         else:
    #             results[rec] = 1
    #
    # if recipes:
    #     logging.warning("Adding recipes")
    #     for rec in recipes:
    #         if rec in results:
    #             results[rec] += 2
    #         else:
    #             results[rec] = 2

    return results


def sort(final_results):
    new_dict = OrderedDict(sorted(final_results.items(), key=lambda x: x[1], reverse=True))
    return list(new_dict.keys())


