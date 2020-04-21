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
    except Exception as e:
        print('ERROR: request failed')
        print(str(e))

def run_tasks():
    while len(task_queue) > 0:
        task = task_queue.pop()
        data = task()
        print(data)
        protected_data = []
        for recipe in data:        
            if not type(recipe) == Recipe:
                print('WARNING: Task %s does not return correctly formatted data' % str(task))
            else:
                protected_data.append(recipe())
        post_scraped_data(protected_data)


def docker_shutdown(a,b):
    #add any additional cleanup here
    sys.exit()

def main():
    schedule.every().sunday.at("04:00").do(run_tasks)
    try:
        while True:
            schedule.run_pending()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":

    signal.signal(signal.SIGTERM, docker_shutdown)
    signal.signal(signal.SIGINT, docker_shutdown)
    main()
