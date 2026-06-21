import signal
import sys
from loguru_playground.generator.main import run_forever


def handle_exit(sig, frame):
    print("\nStopping log generator.")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)


if __name__ == "__main__":
    for log in run_forever(interval_sec=0.5):
        print(log)
