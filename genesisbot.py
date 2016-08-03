from nltk.book import text3 as genesis
import random

def populate_monte_carlo(text):
    monte_carlo = {}
    word_buffer = []
    for word in text:
        if len(word_buffer) == 3:
            key = "{WORD1} {WORD2}".format(WORD1=word_buffer[0], WORD2=word_buffer[1])
            if key in monte_carlo:
                monte_carlo[key].append(word_buffer[2])
            else:
                monte_carlo[key] = [word_buffer[2]]
            word_buffer.pop(0)
        if word.isalpha():
            word_buffer.append(word)
    return monte_carlo


def create_sentence(monte_carlo, max_length):
    initial_key = random.choice(list(monte_carlo.keys()))
    sentence = initial_key.split()
    while len(sentence) < max_length:
        key = "{WORD1} {WORD2}".format(WORD1=sentence[-2], WORD2=sentence[-1])
        options = monte_carlo[key]
        if options:
            sentence.append(random.choice(options))
        else:
            return sentence
    return sentence


if __name__ == "__main__":
    monte_carlo = populate_monte_carlo(genesis)
    print(" ".join(create_sentence(monte_carlo, 20)))

