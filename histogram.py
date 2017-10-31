import random
from functools import reduce

#read_file = word_file.read()
#split_file = read_file.split()
word_list = ["Rohan", "Willie", "Elliot", "Tia", "Matt", "Captain Rainbow", "Alan", "Braus"]

def find_consistency_of_words(user_input, word_list):
    word_consistancy = {}
    # Key value must pair where the key represents the unique word
    if user_input in word_list:
        occurence = word_list.count(user_input)
        print(occurence)
        word_frequency[user_input] = occurence
    return word_frequency

def find_unique_word(word_list):
    unique_word = []
    for word in word_list:
        occurences = word_list.count(word)
        if occurences == 1:
            unique_word.append(word)
    return "Unique words are %s" %(unique_word)
word_frequency = {}
def histogram(word_list):
    # Take the unique word as the key of the dictonary

    for word in word_list:
        occurences = word_list.count(word)
        print(occurences)
        word_frequency[word] = occurences
    return word_frequency

def generate_random_word():
    user_input = str(input()).split()
    for word in histogram(user_input):
        random_index = random.randint(0, len(user_input) -1)
        random_word = user_input[random_index]
    return random_word

def generate_weights(word_list):
    weight_dictionary = {}
    sum_values = sum(histogram(word_list).values())
    for word in word_list:
        word_occurences = word_list.count(word)
        weight_occurences = word_occurences / sum_values
        weight_dictionary[word] = weight_occurences
    return weight_dictionary

def list_of_tuples_histogram():
    list_of_turples = list((zip(histogram(word_list).keys(), histogram(word_list).values())))
    return list_of_turples

def list_of_histogram():
    base_list = []
    for key, value in histogram(word_list).items():
        structured_list = [key, value]
        base_list.append(structured_list)
    return base_list

print(histogram(word_list))
