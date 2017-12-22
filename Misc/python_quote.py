import sys
from random import randrange
import time

with open(".txt", "r") as r:
    words = r.read()


def create_quote(length):

    quote = ""

    for i in range(length):
        lines = words.splitlines()
        line_number = randrange(0, len(lines))
        word = lines[line_number]

        if i == length -1:
           quote += (word + ".")
        else:
            quote += (word + " ")

    return quote

if __name__ == "__main__":
    time_before = time.time()
    quote_length = int(sys.argv[-1])
    quote = create_quote(quote_length)
    print(quote)
    time_after = time.time()
    print(time_before - time_after)