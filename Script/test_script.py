from sys import stdout
from time import sleep 

def slow(text, delay=0.03):
    if text: # only process if the string is not zero length
        for c in text:
            print(c, end='', flush=True)
            sleep(delay)
        if text[-1] != '\n':
            print()

slow("Hello world!")