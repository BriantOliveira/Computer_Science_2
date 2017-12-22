import sys, string, re, time
from operator import itemgetter
import cleanup as c


def histogram_dict(text_list):
    """
    Return a histogram dictionary structure
    """
    dictogram = {}
    get = dictogram.get

    for word in text_list:
        dictogram[word] = get(word, 0) + 1
    return dictogram

def histogram_list(clean_txt):
    """
    Store unique word and frequency in a list
    """
    word_frequency = []
    for word in range(0, len(clean_txt) -1):
        word = clean_txt[word]
        frequency = clean_txt.count(word)
        initial_list = [word, frequency]
        if initial_list not in word_frequency:
            word_frequency.append(initial_list)
    # Search by the frequency of word
    word_frequency = sorted(word_frequency, key=itemgetter(1))
    print(word_frequency)
    return word_frequency

def histogram_tuples_list(text_list):
    """
    Store unique word and frequency in a list of tuple
    """
    word_frequency = []
    for word in range(0, len(text_list) -1):
        word = text_list[word]
        frequency = text_list.count(word)
        initial_tuple = (word, frequency)
        if initial_tuple not in word_frequency
