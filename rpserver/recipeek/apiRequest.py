import requests
import json
import spoonacular as sp

def getRecipes():
    API_KEY = "d1417a3a8f0c4abab57d01a7428b3e15"
    result = requests.get("https://api.spoonacular.com/recipes/search?query=apples&number=2" + "&apiKey=" + API_KEY)
    json_response = json.loads(result.text)
    recipes = json_response['results']

    # for recipe in recipes:
    #     print(recipe['title'])
    #     title = recipe['title']
    #     image_url = recipe['imageURLs']

    print(json_response)

getRecipes()

# api = sp.API("d1417a3a8f0c4abab57d01a7428b3e15")

# # Parse an ingredient
# # response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
# # data = response.json()
# # print(data[0]['name'])

# # # Get a random food joke
# # response = api.get_a_random_food_joke()
# # data = response.json()
# # print(data['text'])

# # # Detect text for mentions of food
# # response = api.detect_food_in_text("I really want a cheeseburger.")
# # data = response.json()
# # print(data['annotations'][0])


# # Search Recipe
# response = api.search_recipes("Chicken fried rice")
# data = response.json()
# print(data)

# import requests

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

# querystring = {"diet":"vegetarian","excludeIngredients":"coconut","intolerances":"egg%2C gluten","number":"10","offset":"0","type":"main course","query":"burger"}

# headers = {
#     'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
#     'x-rapidapi-key': "3b3cde449amsh37ba2c9857841d5p1d915bjsn273110e858e7"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)