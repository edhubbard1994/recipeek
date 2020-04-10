from django.test import TestCase

# Create your tests here.
import requests

def test():
    url = 'http://localhost:8000/api/search/'
    r = requests.post(url, data={'keywords': 'gluten-free paprika'})
    recipes = r.json()
    return recipes

if __name__ == "__main__":
    test()