from scrape import Recipe, Ingredient, scrape_task
import requests
import time
import os


query_params1 = ['fish','salmon','potato','cake']
query_params2 = ['pie','goat', 'lamb','stew','bread']
query_params3 = ['nut', 'spicy', 'sweet', 'bbq','pasta'] 
query_params4 = ['italian', 'american', 'sushi', 'catfish', 'almond']
query_params5 = ['peanut','ginger','garlic','pizza','corn']
query_params6 = ['fried','baked','grilled','roasted','sandwich']

def collect_ingredients(ingredients):
    acc = []
    for ingredient in ingredients:
        amount = 0
        arr = ingredient['text'].split(' ')
        try:
            amount = int(arr[0])
        except:
            amount = 1
        i = Ingredient(
            ingredient['text'],
            amount,
            'each',
        )
        acc.append(i)
    return acc




def edamam_api_call(query):
    APP_ID = os.environ['EDAMAM_APP_ID']
    API_KEY = os.environ['EDAMAM_API_KEY']
    url = 'https://api.edamam.com/search?q=%s&app_id=%s&app_key=%s' % (query,APP_ID,API_KEY)
    r = requests.get(url)
    recipes = r.json()
    #print(recipes['hits'][0]['recipe'])
    #print(recipes['hits'][0]['recipe']['ingredients'])
    acc = []
    try:
        for i in range(len(recipes['hits'])):
            ingredients = recipes['hits'][i]['recipe']['ingredients']
            recipe = recipes['hits'][i]['recipe']
            labels = []    
            if 'healthLabels' in recipe.keys():
                labels.extend(recipe['healthLabels']) 
            if 'dietLabels' in recipe.keys():
                labels.extend(recipe['dietLabels']) 
            print(labels)
            recipe_ob = Recipe(
                recipe['label'],
                recipe['url'],
                'unknown',
                collect_ingredients(ingredients),
                recipe['image'],
                recipe['calories'],
                labels
            )
            acc.append(recipe_ob)
        return acc
    except Exception as e:
        print(str(e))
        return []

@scrape_task
def collect_api_calls1():
    acc = []
    for query in query_params1:
        acc.extend(edamam_api_call(query))
        time.sleep(12)
    return acc

@scrape_task
def collect_api_calls2():
    acc = []
    for query in query_params2:
        acc.extend(edamam_api_call(query))
        time.sleep(12)
    return acc

@scrape_task
def collect_api_calls3():
    acc = []
    for query in query_params3:
        acc.extend(edamam_api_call(query))
        time.sleep(12)
    return acc

@scrape_task
def collect_api_calls4():
    acc = []
    for query in query_params4:
        acc.extend(edamam_api_call(query))
        time.sleep(12)
    return acc
    
@scrape_task
def collect_api_calls5():
    acc = []
    for query in query_params5:
        acc.extend(edamam_api_call(query))
        time.sleep(12)
    return acc

@scrape_task
def collect_api_calls6():
    acc = []
    for query in query_params6:
        acc.extend(edamam_api_call(query))
        time.sleep(12)
    return acc
