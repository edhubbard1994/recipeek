import signal
import sys
import datetime

def docker_shutdown():
    sys.exit()

if __name__ == "__main__":

    signal.signal(signal.SIGTERM, docker_shutdown)
    signal.signal(signal.SIGINT, docker_shutdown)

    try:
        while True:
            pass

    except KeyboardInterrupt:
        sys.exit()
