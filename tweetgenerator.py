import random



quotes = ("Stu: Why can't we remember ANYTHING that happened last night?",
          "Alan: That's one of the side-effects of Roofies. Memory loss.",
          "Stu: You are literally too stupid to insult.","Alan: Thank You!")

def random_python_quotes():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quotes()
    print(quote)
