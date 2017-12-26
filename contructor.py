import histogram as h
import cleanup as c
import random, sys, re
import markov as m
from pprint import pprint
from collections import word_frequency


def create_dictionary_from_list(clean_list):
    """Take a list and return an dictionary"""

    list_of_pairs = []

    for index in range(0, len(clean_list) -1):
        current = clean_list[index]
        next = clean_list[index + 1]
        list_of_pairs.append((current, next))
    dictionary = h.histogram_dict(list_of_pairs)
    return dictionary

def get_random_word(dictionary):
    """
    Return a tuple from a dictionary
    """
    rand_index = random.randint(0, len(dictionary) -1)
    key_list = list(dictionary)
    random_word = key_list[rand_index]
    return random_word

def _probability_(dictionary):
    """
    Get a random word and dictionary and return new dictionary
    """
    total_tokens = sum(dictionary.values())
    dictionary_with_weight = {}

    for (word, value) in dictionary.items():
        weight = float(value / total_tokens)
        dictionary_with_weight[word] = weight
        del dictionary_with_weight[('dream', 'STOP')]
        return dictionary_with_weight
