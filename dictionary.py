import random
import time

'''This function will take a list and create random grouping of those words'''

dictionary_of_words = {'happiness': 'good fortune; pleasure; contentment; joy.',
                       'sad': 'affected by unhappiness or grief; sorrowful or mournful',
                        'mournful': 'feeling or expressing sorrow or grief; sorrowful; sad'}

def random_argument(split_file):
    array_of_arguments = []
    for _ in range(10):
        random_index = random.randint(0, len(split_file) -1)
        array_of_arguments.append(split_file[random_index])
    return " ".join(array_of_arguments)

referance_keys = dictionary_of_words.keys()
random_key = random.choice(list(referance_keys))
key_index = list(dictionary_of_words.keys()).index(random_key)

def creating_promp_to_user(dictionary_of_words):
    print("Guess the definition of the word %s" %(random_key))
    user_input = str(input())
    if user_input is not None:
        print ("The correct definition is %s" %(dictionary_of_words[random_key]))
    return ''

'''
if __name__ == '__main__': 
    start_time = time.time()
    print(random_argument(slipt_file))
    end_time = time.time()
    print(end_time - start_time) m 
'''
