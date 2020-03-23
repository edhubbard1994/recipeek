from scrape import Recipe, Ingredient, scrape_task
import requests

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

@scrape_task
def edamam_api_call():
    url = 'https://api.edamam.com/search?q=chicken&app_id=84ccbee5&app_key=d8004719869b5827b1a5aa5b3256fdfc&from=0&to=3&calories=591-722&health=alcohol-free'
    r = requests.get(url)
    recipes = r.json()
    #print(recipes['hits'][0]['recipe'])
    #print(recipes['hits'][0]['recipe']['ingredients'])
    acc = []
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

    
