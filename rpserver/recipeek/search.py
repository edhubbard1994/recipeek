from .models import *
from collections import OrderedDict
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
import logging

def search_recipes_sorted(keywords):
    final_results_weighted = {}
    words_to_filter = []

    for word in keywords.split():
        if word.startswith("has:"):
            logging.warning(word)
            logging.warning(word[4:])
            words_to_filter.append(word[4:])
        else:
            logging.warning(word)
            results = search(word)
            for recipe in results:
                if recipe in final_results_weighted.keys():
                    final_results_weighted[recipe] += results[recipe]
                else:
                    final_results_weighted[recipe] = results[recipe]

    filtered_list = filterByKeywords(words_to_filter, final_results_weighted)

    return sort(filtered_list)

def search(word):
    # ingredients = Ingredient.objects.filter(name__icontains=word)
    # cuisines = Cuisine.objects.filter(name__icontains=word)
    # diets = Diet.objects.filter(name__icontains=word)
    recipes = Recipe.objects.filter(title__icontains=word)

    results = {}
    # 
    # for recipe in recipes:
    #     results[recipe] = 1

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

    if recipes:
        for rec in recipes:
            if rec in results:
                results[rec] += 2
            else:
                results[rec] = 2

    return results

def filterByKeywords(words_to_filter, final_results_weighted):
    final_filtered_recipes = final_results_weighted.copy()

    for recipe in final_results_weighted.keys():
        should_delete = False

        for word in words_to_filter:
            if word.lower() not in recipe.title.lower():
                should_delete = True

        if should_delete:
            final_filtered_recipes.pop(recipe)

    return final_filtered_recipes

def sort(final_results):
    new_dict = OrderedDict(sorted(final_results.items(), key=lambda x: x[1], reverse=True))
    return list(new_dict.keys())
