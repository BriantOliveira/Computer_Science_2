from string import punctuation

class Clean():

    def __init__(self):
        pass

    def _erase_pontuation(self, file_name):
        with open(file_name, 'r') as myfile:
            dialouge_list = myfile.read()
        long_string = ''.join(dialouge_list)
        long_string = ''.join(c for c in long_string if c not in punctuation)
        return long_string

    def single_words(self, long_string):
        word_list = long_string.lower()
        word_list = word_list.split()
        return word_list

    def text_cleaner(self, file_name):
        long_string = self._erase_pontuation(file_name)
        word_list = self.single_words(long_string)
        return word_list


file_name = "harry_potter_books.txt"
Clean().text_cleaner(file_name)
print(file_name)
