from scrape import Recipe, Ingredient, scrape_task
import requests
import time

query_params1 = ['mediterranean','chinese','american','indian']
query_params2 = ['healthy','vegan', 'chicken','rice','breakfast']
query_params3 = ['lunch', 'dinner', 'snack', 'fruit','mexican'] 
query_params4 = ['southern', 'comfort', 'steak', 'carribean', 'sides']
query_params5 = ['soul','kosher','halal','vegetarian']

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
