import signal
import sys
import datetime
import schedule
import scrape


task_queue = []


def run_tasks():
    collected_data = []
    while len(task_queue) > 0:
        task = task_queue.pop()
        data = task()
        collected_data.extend(data)
    print(collected_data)

def docker_shutdown():
    #add any additional cleanup here
    sys.exit()

def main():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":

    signal.signal(signal.SIGTERM, docker_shutdown)
    signal.signal(signal.SIGINT, docker_shutdown)
    main()
