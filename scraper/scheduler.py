import signal
import sys
import datetime


class Scheduler:

    def __init__(self):
        self.


def docker_shutdown():
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
