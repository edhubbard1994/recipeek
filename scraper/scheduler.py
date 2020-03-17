import signal
import sys
import datetime
import schedule
import scrape


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
