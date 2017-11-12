import cleanup
import pdb

class Listogram(list):
    def __init__(self, word_text):
        self.word_text = word_text

    def listogram(self):
        dictionary_occurences = {}
        dictionary_word = {}
        histogram_list = []
        pairs_of_histogram = ()
        cleaned_text = cleanup.cleaned_given_text(self.word_text)[:100]
        for word in cleaned_text:
            word_tuple = (word, )
            word_occurences = cleaned_text.count(word)
            occurences_in_dictionary_words[word] = word_occurences
            if word not in pairs_of_histogram:
                pairs_of_histogram = word_tuple + (word_occurences, )
                print("\"{}\" appears {} times".format(word, word_occurences))
            if pairs_of_histogram not in histogram_list:
                histogram_list.append(pairs_of_histogram)
            print('%s tokens, %s types' %(sum(dictionary_occurences.values()), len(dictionary_occurences)))
            return histogram_list

    def frequency_of_certain_word(self):
        certain_list_of_pair_of_word = []
        user