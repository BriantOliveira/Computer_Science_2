import random

list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish", "two"]
probablities = {}


def choose_word(list, probabilities):
    assert len(list) == len(probabilities)
    assert 0 <= min(probabilities) and max(probabilities) <1
    assert abs(sum(probabilities) -1.0) < 1.0e-5
    random_pick = random.uniform(0, 1)
    cumulative_probability = 0.0
    for word,  word_probability in zip(list, probabilities):
        cumulative_probability += word_probability
        if random_pick < cumulative_probability:
            break
        return word

