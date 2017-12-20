from pprint import pprint
from time import time as t
from random import random as ri
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
    cur_position = self.select
