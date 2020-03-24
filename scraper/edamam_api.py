from scrape import Recipe, Ingredient, scrape_task
import requests
import time

querey_params = ['mediterranean','chinese','american']

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
    url = 'https://api.edamam.com/search?q=%s&app_id=84ccbee5&app_key=d8004719869b5827b1a5aa5b3256fdfc' % query
    r = requests.get(url)
    recipes = r.json()
    #print(recipes['hits'][0]['recipe'])
    #print(recipes['hits'][0]['recipe']['ingredients'])
    acc = []
    try:
        for i in range(len(recipes['hits'])):
            ingredients = recipes['hits'][i]['recipe']['ingredients']
            recipe = recipes['hits'][i]['recipe']
            recipe_ob = Recipe(
                recipe['label'],
                recipe['url'],
                'unknown',
                collect_ingredients(ingredients),
                recipe['image'],
                recipe['calories']
            )
            acc.append(recipe_ob)
        return acc
    except:
        return []

@scrape_task
def collect_api_calls():
    acc = []
    for query in querey_params:
        acc.extend(edamam_api_call(query))
        time.sleep(0.5)
    return acc
    
#print(edamam_api_call())