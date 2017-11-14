import split_array
import pdb

class Dictogram(dict):
    def __init__(self, word_text):
        self.word_text = word_text

    def create_histogram(self):
        frequency_of_word = {}
        cleaned_text = split_array.clean_given_text(self.word_text)[:100]
        for word in cleaned_text:
            occurences_of_the_word = cleaned_text.count(word)
            frequency_of_word[word] = occurences_of_the_word
        return frequency_of_word

    def weights_of_histogram(self):
        '''Create the weights or the occurences of the words'''
        dictionary_weight = {}
        sum_values = sum(self.create_histogram().values())
        cleaned_text = split_array.clean_given_text(self.word_text)
        for word in cleaned_text:
            occurences_of_word = self.word_text.count(word)
            occurences_weight = occurences_of_word / sum_values
            dictionary_weight[word] = occurences_weight
        return dictionary_weight

    def frequency_of_given_word(self, user_input):
        '''find frequency of the word of user input'''
        given_word_frequency = {}
        user_input = str(input())
        cleaned_text = split_array.clean_given_text(self.word_text)
        if user_input in cleaned_text:
            occurence_on_given_word = cleaned_text.count(user_input)
            frequency_on_given_word[user_input] = occurence_on_given_word
        else:
            return 'This word does not occures'
        return given_word_frequency

dictogram = Dictogram('hangover_movie_script.txt')

print(dictogram.frequency_of_given_word("the"))