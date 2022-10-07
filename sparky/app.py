import signal
import sys
import concurrent.futures

from sparky.modules.head import Head

def handler(signum, handler):
    print('Signal handler called with signal', signum)
    sys.exit()

def run():
    print("Hello, I am Sparky")

    signal.signal(signal.SIGINT, handler)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        process_head = executor.submit(Head)

if __name__ == "__main__":
    run()
