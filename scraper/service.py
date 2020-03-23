import requests
from rpserver.recipeek.models import Recipe

# def get_recipes_api():
#     # url = 'https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=79fc7319904f45df944d73e6682a1163'
#     url = 'https://api.edamam.com/search?q=chicken&app_id=84ccbee5&app_key=d8004719869b5827b1a5aa5b3256fdfc&from=0&to=3&calories=591-722&health=alcohol-free'
#     r = requests.get(url)
#     recipes = r.json()
#     print(recipes)
#     recipe_list = []
#     for i in range(len(recipes['hits'])):
#         recipe_list.append(recipes['hits'][i]['recipe'])
#         print(recipes['hits'][i]['recipe'])
#     return recipe_list
#
def get_recipes_api_2():
    # url = 'https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=79fc7319904f45df944d73e6682a1163'
    url = 'https://api.edamam.com/search?q=chicken&app_id=84ccbee5&app_key=d8004719869b5827b1a5aa5b3256fdfc&from=0&to=3&calories=591-722&health=alcohol-free'
    r = requests.get(url)
    recipes = r.json()
    print(recipes)
    recipe_list = []
    for i in range(len(recipes['hits'])):
        recipe = recipes['hits'][i]['recipe']
        print(recipe)
        print("\n")
        # recipe_list.append(recipes['hits'][i]['recipe'])
        curr_recipe = Recipe.objects.get(id=recipe['uri'])
        print("gotten!")
        if not curr_recipe:
            r = Recipe(id=recipe['uri'], title=recipe['label'], image_url=recipe['image'], recipe_url=recipe['url'],
                       calories=recipe['calories'])
            r.save()
            print("added!")
#
# if __name__ == "__main__":
#     get_recipes_api_2()