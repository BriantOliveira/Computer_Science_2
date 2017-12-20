import sys
import string
import re

""" Clean text files"""


def clean_txt(filename):
    txt_file = open(filename, 'r')
    word_list = txt_file.read().lower()
    remove_punctuation(word_list)
    result_list = []

    items = re.findall("[A-z]+\'?[A-z]*\$[0-9]*", word_list)
    for item in items:
        result_list.append(item)
    return result_list

def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    no_punc_text = re.sub(':', ' ', no_punc_text)
    no_punc_text = re.sub('/(?<!\S).(?!\S)\s*/', '', no_punc_text)
    return no_punc_text


def main():
    user_arg_count = len(sys.argv)
    if user_arg_count 1:
        print('Error: textfile not provided')
    else:
        txt_file = open(sys.argv[1], 'r')
        word_list = txt_file.read().lower()
        print(word_list)

        items = re.findall("[A-z]+\'?[A-z]*|\$[0-9]*", word_list)
        for item in items:
            print(item)


if __name__ == '__main__':
    main()
