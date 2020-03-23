from scrape import Recipe, Ingredient, scrape_task
import requests
from bs4 import BeautifulSoup




def make_top_request(query):
    req = requests.get('https://api.edamam.com/recipes/%s' % str(query))
    soup = BeautifulSoup(req.text,features='html5lib')
    uls = soup.findAll('section',recursive=True)
    for i in uls:
        print(i)



@scrape_task
def edamam_scraper():
    pass


make_top_request('fish')
