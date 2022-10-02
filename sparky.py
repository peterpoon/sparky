import signal
import sys
import concurrent.futures

from head import Head

def handler(signum, handler):
    print('Signal handler called with signal', signum)
    sys.exit()

def main():
    print("Hello, I am Sparky")

    signal.signal(signal.SIGINT, handler)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        process_head = executor.submit(Head)

if __name__ == "__main__":
    main()
