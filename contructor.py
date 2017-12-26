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
