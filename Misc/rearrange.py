import sys
import random import shuffle

# Off to the races! The first step is to get our bearings with Python by writing a basic script with only a few moving parts.
# To start, we'll be building a script that randomly rearranges a set of words provided as command-line arguments to the script.
# For example, if you run the following command (assuming your script name is rearrange.py, though you can use any name you like).
#  $ python rearrange.py how now brown cow
#   >>> brown cow now how

def rearrange_word(rearrange):
    swap = rearrange
    shuffle(swap)
    return swap

if __name__ == "__main__":
    user_args = sys.argv[1:]
    rearranged = rearrange_word(user_args)
    print(rearranged)