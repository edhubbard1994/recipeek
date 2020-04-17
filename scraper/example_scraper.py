from scrape import Ingredient, Recipe, scrape_task #required from scrape API
import bs4 #beautiful soup if webscraping


# declare the decorator befor every scrape function
# helper functions are fine but the main one you want ran
# must have this decorator to work
@scrape_task
def example():

    # Process all data collected from the web into Ingredients and Recipes
    # All data will be parsed later into json. 
    in1 = Ingredient('sugar','1/2','tbsp')
    in2 = Ingredient('spice','1/4','tbsp')
    in3 = Ingredient('everything nice', '1/8','tbsp')
    r = Recipe('soup','http://soup.com','vegan',[])

    # You have to return an iterable of recipes regardless of how many there
    # actually are
    return [r]

# Be sure to import your scraper python file in scheduler.py as well


# the below example will silently fail because the return type is not an
# iterable of Recipes. A WARNING will be printed when ran
@scrape_task
def bad_example():
    return ['hello'] 
