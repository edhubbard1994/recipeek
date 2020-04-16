from django.db.models import Q

from .models import *
from collections import OrderedDict

def search_recipes_sorted(keywords):
    final_results_weighted = {}
    words_to_filter = {'has': [], 'diet': []}

    for word in keywords.split():
        if word.startswith("has:"):
            words_to_filter['has'].append(word[4:])
        elif word.startswith("diet:"):
            words_to_filter['diet'].append(word[5:])
        else:
            results = search(word)
            for recipe in results:
                if recipe in final_results_weighted.keys():
                    final_results_weighted[recipe] += results[recipe]
                else:
                    final_results_weighted[recipe] = results[recipe]

    filtered_list = filterByKeywords(words_to_filter, final_results_weighted)

    return sort(filtered_list)

def search(word):
    # cuisines = Cuisine.objects.filter(name__icontains=word)

    recipes = Recipe.objects.filter(Q(title__icontains=word) | Q(recipe_url__contains=word))
    diet_recipes = Recipe.objects.filter(diet__icontains=word)
    results = {}

    #Increments weight of each recipe by a predetermined amount.
    #Recipe title is weighted higher, and so are multiple matches.
    # if cuisines:
    #     cuisine_recipes = Recipe.objects.filter(cuisine__name=cuisines[0].name)
    #     for rec in cuisine_recipes:
    #         if rec in results:
    #             results[rec] += 1
    #         else:
    #             results[rec] = 1

    if diet_recipes:
        for rec in diet_recipes:
            if rec in results:
                results[rec] += 6
            else:
                results[rec] = 6

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

        if 'has' in words_to_filter.keys():
            for word in words_to_filter['has']:
                if word.lower() not in recipe.title.lower():
                    should_delete = True

        if 'diet' in words_to_filter.keys():
            for word in words_to_filter['diet']:
                if word.lower() not in recipe.diet.lower():
                    should_delete = True

        if should_delete:
            final_filtered_recipes.pop(recipe)

    return final_filtered_recipes

def sort(final_results):
    new_dict = OrderedDict(sorted(final_results.items(), key=lambda x: x[1], reverse=True))
    return list(new_dict.keys())
