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

def generate_weights(word_list):
    weight_dictionary = {}
    sum_values = sum(histogram(word_list).values())
    for word in word_list:
        word_occurences = word_list.count(word)
        weight_occurences = word_occurences / sum_values
        weight_dictionary[word] = weight_occurences
    return weight_dictionary

def list_of_tuples_histogram():
    #This function will make histogram into a list of turples
    base_list = []
    structured_turple = ()

    for word in word_list:
        word_tuple = (word, )
        occurences = word_list.count(word)
        word_occurences = occurences
        if word not in structured_turple:
            structured_turple = word_tuple + (word_occurences, )
        if structured_turple not in base_list:
            base_list.append(structured_turple)
    second_element = [x[1] for x in base_list]
    return second_element

def create_weight_using_turple(word_list):
    general_list = []
    main_turple = ()
    sum_values = sum(list_of_tuples_histogram(word_list))

    for word in word_list:
        weighted_occurences = word_list.count(word) / sum_values
        word_turple = (word, )
        if word not in main_turple:
            main_turple = word_turple + (weighted_occurences, )
        if main_turple not in general_list:
            general_list.append(main_turple)
    return general_list

def list_of_histogram(word_list):
    general_list = []
    main_list = []
    for word in word_list:
        occurences = word_list.count(word)
        if word not in main_list:
            main_list = [word, occurences]
        if main_list not in general_list:
            general_list.append(main_list)
    second_element = [x[1] for x in general_list]
    return second_element

def creating_random_word_histogram():
    # Will generate a random word
    for word in word_list:
        random_index = creating_randomness.gen_random_range(0, len(word_list) -1)
        random_word = word_list[random_index]
    return random_word



print(histogram(word_list))
