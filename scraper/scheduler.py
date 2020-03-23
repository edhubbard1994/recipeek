import signal
import sys
import datetime
import schedule
from scrape import Recipe, get_tasks
import copy
import requests
import json
import time


### Import Individual Scrapers Here ###
import example_scraper
import edamam_api
###


task_queue = copy.copy(get_tasks())


def post_scraped_data(data):
    time.sleep(10)
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    print(data)
    try:
        req = requests.post('http://backend:8000/api/import/',data=json.dumps(data),headers=headers)
    except:
        print('ERROR: request failed')

def run_tasks():
    collected_data = []
    while len(task_queue) > 0:
        task = task_queue.pop()
        data = task()
        protected_data = []
        for recipe in data:        
            if not type(recipe) == Recipe:
                print('WARNING: Task %s does not return correctly formatted data' % str(task))
            else:
                protected_data.append(recipe())
        collected_data.extend(protected_data)
    post_scraped_data(collected_data)

def docker_shutdown(a,b):
    #add any additional cleanup here
    sys.exit()

def main():
    run_tasks()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":

    signal.signal(signal.SIGTERM, docker_shutdown)
    signal.signal(signal.SIGINT, docker_shutdown)
    main()
