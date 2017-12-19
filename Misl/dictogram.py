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

    # def pair_together(self):
    #     '''Pairs given body together'''
    #     text_paired = {}
    #     cleaned_text = split_array.clean_text(self.word_text)
    #     rare_word = max(self.create_histogram().values())
    #     for word in range(len(cleaned_text[:10]) -1):
    #         text_paired[cleaned_text[word]] = {cleaned_text[word + 1] }
    #     return text_paired


    def look_for_word_entered(self, user_input):
       pair_list = list(self.pair_together())
       new_word = pair_list.index(user_input)
       return pair_list[new_word]

    def all_words(self):
        list_of_words = []
        cleaned_text = split_array.clean_text(self.word_text)[:100]
        for word in cleaned_text:
            list_of_words.append(word)
        return list_of_words

    def build_states_and_transitions(self):
        '''Find the state and trasition'''
        word_list = []
        probability_of_word = {}
        dictionary_chain = {}
        pair_list = list(self.pair_together())
        count = 0

        while count != (len(pair_list) -1):
            for word in self.all_words():
                next_word = self.all_words().count(self.look_for_word_entered(word))
            current_word = self.all_words().count(word)
            probability = next_word / current_word
            new_word = self.all_words().index(word) + 1
            new_word_values = pair_list[new_word]
            dictionary_chain[word] = {self.look_for_word_entered(new_word_values): probability_of_word}
            count = count + 1
        return dictionary_chain


#dictogram = Dictogram('hangover_movie_script.txt')
cleaned_text = split_array.clean_text('hangover_movie_script.txt')[:100]

'''create dictionary that the current word is the key while the value is a dictionaty'''
def markov_chain(cleaned_text):
    print(cleaned_text)
    markov_dictionary = {}
    x = 0
    while x < len(cleaned_text) -1:
        current_word = cleaned_text[x]
        next_word = cleaned_text[x + 1]
        if current_word not in markov_dictionary.keys():
            markov_dictionary[current_word] = Dictogram()
        markov_dictionary[current_word].adding_count(next_word)
        x += 1

        return markov_dictionary


#print(dictogram.frequency_of_given_word("the"))
print(markov_chain("one fish two fish red fish blue fish".split()))
