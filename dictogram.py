import split_array
import pdb

class Dictogram(dict):
    def __init__(self, word_text):
        self.word_text = word_text

    def create_histogram(self):
        frequency_of_word = {}
        cleaned_text = split_array.clean_text(self.word_text)[:1000]
        for word in cleaned_text:
            occurences_of_the_word = cleaned_text.count(word)
            frequency_of_word[word] = occurences_of_the_word
        return frequency_of_word

    def adding_count(self, word, count=1):
        if word not in self:
            self[word] = count
        else:
            self[word] += count

    def weights_of_histogram(self):
        '''Create the weights or the occurences of the words'''
        dictionary_weight = {}
        sum_values = sum(self.create_histogram().values())
        cleaned_text = split_array.clean_text(self.word_text)[:1000]
        for word in cleaned_text:
            occurences_of_word = self.word_text.count(word)
            occurences_weight = occurences_of_word / sum_values
            dictionary_weight[word] = occurences_weight
        return dictionary_weight

    def frequency_of_given_word(self, user_input):
        '''find frequency of the word of user input'''
        given_word_frequency = {}
        user_input = str(input())
        cleaned_text = split_array.clean_text(self.word_text)[:1000]
        if user_input in cleaned_text:
            occurence_on_given_word = cleaned_text.count(user_input)
            given_word_frequency[user_input] = occurence_on_given_word
        else:
            return 'This word does not occures'
        return given_word_frequency

    def look_for_rare_word(self):
        rare_word = {}
        high_occurence = max(self.create_histogram().values())
        for key, value in self.create_histogram().items():
            if value == high_occurence:
                rare_word[key] = value
        return rare_word

    def pair_together(self):
        '''Pairs given body together'''
        text_paired = {}
        cleaned_text = split_array.clean_text(self.word_text)
        rare_word = max(self.create_histogram().values())
        for word in range(len(cleaned_text[:10]) -1):
            text_paired[cleaned_text[word]] = {cleaned_text[word + 1]: }
        return text_paired


    def look_for_word_entered(self, user_input):
       pair_list = list(self.pair_together())
       new_word = pair_list.index(user_input)
       return pair_list[new_word]

    def all_words(self):


dictogram = Dictogram('hangover_movie_script.txt')

print(dictogram.frequency_of_given_word("the"))