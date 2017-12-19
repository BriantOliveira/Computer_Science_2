from time import time
import math

word_list = ["Elliot Oliveira", "John Snow", "Brandon Stark", "John Snow", "Sansa Skark", "Danerys"]

def time_random():
    return (time() - float(str(time()).split('.')[0]))

def random_range(min, max):
    return float(time_random() * (min + max) - min())

#print(random_range)