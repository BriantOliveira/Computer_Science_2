from pprint import pprint
from time import time as t
import random as ri
import sys


class Markov_chain_Nth_order(object):
    def __init__(self, order=1):
        self.states = {}

        if order > 0:
            self.order = order
        else:
            raise Expection("\nInvalid parameter: Integer only.")

    def add_to_chain(self, old, step):
        new = old[1:] + (step, )
        return new

    def create_states(self, tokens):
        """Creating states from the sentences"""
        prev = tuple(tokens[:self.order])

        #Create Markov
        for i in range(self.order, len(tokens)):
            token = tokens[i]

            if prev not in self.states:
                self.states[prev] = []

            cur = self.add_to_chain(prev, token)
            self.states[prev].append(cur)

            prev = cur

        input_sentence = " ".join(tokens)


    def construct_sentence(self):
        """Sample Dictagram and build new sentences"""
        cur_position = self.select_cur_position()
        sentence = ""

        while (cur_position, ) in self.states:
            sentence += " " + cur_position
            cur_position = self.select_cur_position(cur_position)

            if cur_position[-1] == '.':
                break

        return sentence

    def select_cur_position(self, pos=None):
        """Method to select word position in the corpus randomly"""
        if pos is None:
            random_selection = ri.choice(list(self.states))
            cur_position = ''.join(random_selection)
            return cur_position

        state = self.states[(pos, )]
        word = ri.choice(state)
        return ' '.join(word)

    def create_markov_model(self):
        """Create and run class instance, create copus from Harry Potter book"""

        with open("harry_potter_books.txt") as f:
            corpus = f.read().split()

        if len(sys.argv) > 1:
            if sys.argv[1].isnumeric():
                print("Numeric input received successfully... LODING... \n\nORDER OF MARKOV:\nn = {}".format(int(sys.argv[1])))
                markov = Markov_chain_Nth_order(int(sys.argv[1]))

            else:
                print("ERROR INPUT INVALID. REVERTING TO DEFAULT:\n\nORDER OF MARKOV:\nn = 1")
                markov = Markov_chain_Nth_order()
        else:
            print("DID NOT RECEIVED AN INPUT... REVERTING TO DEFAULT:\n\nORDER OF MARKOV:\nn =1")
            markov = Markov_chain_Nth_order()

            # Random walk over then reformating to final sentence
            markov.create_states(corpus)
            random_walk_over = markov.construct_sentence()

            print(random_walk_over)
            output = random_walk_over[0].upper() + random_walk_over[1:]

            print("OUTPUT SENTENCE: {}...".format(output[:140]))
            return



"""
What we are not doing:

- No stocastic sampling
- Look into deque

"""

def main():
    m = Markov_chain_Nth_order(1)
    t0 = t()
    a = m.create_markov_model()
    t1 = t()
    delta = t1 - t0

    print("\n\nTotal runtime is {0:.3g} seconds.\n".format(delta))
    #print(a)
    return


if __name__ == '__main__':
    main()
