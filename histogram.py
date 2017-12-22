import sys, string, re, time
from operator import itemgetter
import cleanup as c


def histogram_dict(text_list):
    dictogram = {}
    get = dictogram.get

    for word in text_list:
        dictogram[word] = get(word, 0) + 1
    return dictogram

def list_histogram(clean_txt):
    word_frequency = []
