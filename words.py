""" words printing for python syntax exercise """

words = ["hello", "hey", "goodbye", "yo", "yes"]



def print_upper_words(words):
    """print upper case strings
    input a list of strings. no return"""

    for word in words:
        print(word.upper())

print_upper_words(words)