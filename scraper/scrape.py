from bs4 import BeautifulSoup



class Ingredient:
    
    def __init__(self,ingrideient, amount, unit, diet=None):
        self.ingredient = ingrideient
        self.amount = amount
        self.unit = unit
        if diet:
            self.diet = diet       

    def __call__(self):
        return self.__dict__ 

class Recipe:

    def __init__(self,title,recipe_url,cuisine,ingredients,image_url=None,calories=None,diet=None):
        self.title = title
        self.recipe_url = recipe_url
        self.cuisine = cuisine
        self.ingredients = [i() for i in ingredients if type(i) == Ingredient]
        if image_url:
            self.image_url = image_url
        if calories:
            self.calories = calories
        if diet:
            self.diet = diet

    def __call__(self):
        return self.__dict__

_task_q = []

def scrape_task(func):
    _task_q.append(func)

def get_tasks():
    return _task_q

