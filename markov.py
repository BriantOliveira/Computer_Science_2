from __future__ import division, print_function

class Markov(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""


    def __init__(self, word_list=None):
        """Initialize the histogram as a new dictogram and count the words given"""
        super(Markov, self).__init__()

        self.types = 0
        self.tokens = 0

        #Count the words given
        if word_list is not None:
            for word in word_list:
                self.add_count(word)


    def add_count(self, word, count=1):
        """ Increase frequency count of given word"""

        if word in self:
            self[word] += count
        else:
            self.types += 1
            self[word] = count
        self.tokens += count


    def frequency(self, word):
        if word not in self:
            return 0
        return self[word]


    def markov_chain(word_list):
        markov = {}
        index = 0
        """Search through the list of words"""
        while index < len(word_list) -1:
            cur_word = word_list[index]
            next_word = word_list[index + 1]

            if cur_word not in markov.keys():
                markov[cur_word] = Markov()
            #if the word is on the dictionary increase count by 1
            markov[cur_word].add_count(next_word)
            index += 1
            return markov

    def second_order_markov_chain(word_list):
        markov = {}
        index = 0

        """ Search through the dictograms"""
        while index < len(word_list) - 2:
            cur_word = word_list[index]
            next_word = word_list[index + 1]
            word_after_next = word_list[index + 2]
            #adding the word to the dictionary
            if(cur_word, next_word) not in markov.keys():
                markov[(cur_word, next_word)] = Markov()
            markov[(cur_word, next_word)].add_count(word_after_next)
            index += 1
        return markov
        print("HERE:", markov)


    def print_histogram(word_list):
        print("print_function: is printing HERE!!!")
        print('word list: {}'.format(word_list))
        #Dictagram display
        histogram = Markov(word_list)
        print('dictogram: {}'.format(histogram))
        print('{} tokens, {} types'.format(histogram.token, histogram.types))
        for word in word_list[-2:]:
            freq = histogram.frequency(word)
            print('{!r} occurs {} times'.format(word, freq))


def main():
    import sys
    import cleanup as clean
    arguments = sys.argv[1:]
    if len(arguments) >= 1:
        print_histogram(arguments)
    else:
        potter_books = clean.clean_txt('onefish.txt')
        #print(potter_books)
        potter_books.append("STOP")
        print(potter_books)
        #markov_dict = second_order_markov_chain()


if __name__ == '__main__':
    main()
