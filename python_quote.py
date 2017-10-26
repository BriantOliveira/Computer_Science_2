import sys
from random import randrange

with open("/user/share/dict/words", "r") as r:
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
    user_args = sys.argv[1]
    quote_length = int(user_args)

    quote = create_quote(quote_length)
    print(quote)