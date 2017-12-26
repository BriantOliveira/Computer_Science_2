import histogram as h
import cleanup as c
import random, sys, re
import markov as m
from pprint import pprint
#from collections import frequency_of_given_word


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

def random_tuple_probability(dictionary_with_weight):
    """
    Select a random word based on it's probability
    """
    random_float = random.random()
    probability = 0.0

    for tpl, word_weight in dictionary_with_weight.items():
        probability += word_weight
        if random_float < probability:
            break
    return tpl


def get_many_random_words(dictionary, num):
    random_dictionary = {}
    while sum(random_dictionary.values()) < int(num):
        random_word = get_random_word_probability(dictionary)
        if random_word not in random_dictionary:
            random_dictionary[random_word] = 1
        else:
            random_dictionary[random_word] += 1
    return random_dictionary

def find_word_after_tuple(tuple_key, markov_dict):
    histogram = markov_dict.get(tuple_key)
    next_random_word = get_random_word(histogram)
    return next_random_word

def find_word_after_random_word(random_word, markov_dict):

    for (types, histogram) in markov_dict.items():
        if types == random_word:
            histogram = markov_dict[types]
            if len(histogram) > 1:
                next_random_word = get_random_word(histogram)
                return next_random_word
            else:
                for (k, v) in histogram.items():
                    next_random_word = k
                    return next_random_word
def create_sentence(word_num, dictionary_with_weight, markov_dict):
    sentence = []
    random_tuple = random_tuple_probability(dictionary_with_weight)
    second_to_last = random_tuple[0]
    last_word = random_tuple[1]
    sentence.append(second_to_last)
    sentence.append(last_word)
    next_word = find_word_after_tuple(random_tuple, markov_dict)

    while len(sentence) < word_num:
        random_tuple = (last_word, next_word)
        second_to_last = last_word
        if next_word != 'STOP':
            sentence.append(next_word)
            next_word = find_word_after_tuple(random_tuple,markov_dict)
        else:
            break
    joined = " ".join(sentence) + "."
    return joined

def clean_text():
    clean_list = c.clean_txt('harry_potter_books.txt')
    clean_list.append("STOP")
    return clean_list

clean_list = clean_text()

def construct_sentence(word_num, clean_list):
    markov_dict = m.second_order_markov_chain(clean_list)
    dictionary =  create_dictionary_from_list(clean_list)
    dictionary_with_weight = _probability_(dictionary)
    random_sentence = create_sentence(word_num, dictionary_with_weight, markov_dict)
    tweet = limit_140_chars(random_sentence)
    print(tweet)
    return tweet

def limit_140_chars(rand_sentence):
    tweet = rand_sentence[0:140]
    tweet = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), tweet, 1)
    tweet = re.sub(' i ', ' I ', tweet)
    tweet = re.sub("i'm", "I'm", tweet)
    tweet = re.sub("i s", "is", tweet)
    tweet = re.sub("i'd", "I'd", tweet)
    tweet = re.sub("does n", "doesn't", tweet)
    tweet = re.sub("doesn t", "doesn't", tweet)
    return tweet
