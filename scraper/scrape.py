from bs4 import BeautifulSoup



class Ingredient:
    
    def __init__(self,ingrideient, amount, unit, diet=None):
        self.ingredient = ingrideient
        self.amount = amount
        self.unit = unit
        if diet:
            self.diet = diet        

class Recipe:

    def __init__(self,title,recipe_url,cuisine,ingredients,image_url=None,calories=None):
        self.title = title
        self.recipe_url = recipe_url
        self.cuisine = cuisine
        self.ingredients = list(ingredients)
        if image_url:
            self.image_url = image_url
        if calories:
            self.calories = calories

    def __call__(self):
        return self.__dict__

r = Recipe('soup','soup.com','vegan',['sugar','spice','everything nice'])
print(r())