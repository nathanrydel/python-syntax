""" words printing for python syntax exercise """

words = ["hello", "hey", "goodbye", "eagle", "E", "yo", "yes"]



def print_upper_words(words):
    """print upper case strings if str starts with e (upper or lowercase)
    input a list of strings. no return"""

    for word in words:
        word = word.upper()
        if word.startswith('E'):
            print(word)

print_upper_words(words)