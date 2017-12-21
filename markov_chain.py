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




    def initialize_chain(self):
        n = self.order
        chain = []

        #tuple with N size
        for _ in range(n):
            chain.append("")

        return tuple(chain)




    def add_to_chain(self, old, step):
        new = old[1:] + (step, )
        return new




    def create_states(self, tokens):
        """Creating states from the sentences"""
        prev = self.initialize_chain()

        #Create Markov
        for token in tokens:
            if not prev in self.states:
                self.states[prev] = []

            cur = self.add_to_chain(prev, token)
            self.states[prev].append(cur)

            prev = cur

        input_sentence = " ".join(tokens)
        print("\nInput Sentece: {}... \n".format(input_sentence[:400]))
        print("WORD COUNT OF CORPUS: >400,000\n")

        return




    def construct_sentence(self):
        """Sample Dictagram and build new sentences"""

        chain = self.initialize_chain()
        cur_position = self.select_cur_position(chain)
        start, delimiter, is_first = "", " ", True

        print("CHAIN: {}\n".format(chain))

        while (cur_position in self.states) and (cur_position != chain) and (cur_position != None):
            if not is_first:
                start += delimiter

                start += cur_position[len(cur_position) -1]
                cur_position = self.select_cur_position(cur_position)
                is_first = False

        walk_over = start + delimiter + cur_position[len(cur_position) -1]

        return walk_over




    def select_cur_position(self, pos):
        """Method to select word position in the corpus randomly"""
        random_selection = ri.choice(list(self.states))
        cur_position = ''.join(random_selection)
        return cur_position


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
            output = random_walk_over[0].upper() + random_walk_over[1:]

            print("OUTPUT SENTENCE: {}...".format(output[:140]))
            return




def main():
    m = Markov_chain_Nth_order(1)
    t0 = t()
    a = m.create_markov_model()
    t1 = t()
    delta = t1 - t0

    print("\n\nTotal runtime is {0:.3g} seconds.\n".format(delta))
    print(a)
    return


if __name__ == '__main__':
    main()
