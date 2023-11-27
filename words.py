""" words printing for python syntax exercise """

def print_upper_words(words, must_start_with):
    """print upper case strings
    if str starts with letter in set (upper or lowercase)
    input a list of strings. no return"""

    for word in words:
        word = word.upper()

        for letter in must_start_with:
            if word.startswith(letter.upper()):
                print(word)
                break

words = ["hello", "hey", "goodbye", "eagle", "E", "yo", "yes"]
must_start_with = {"h", "y"}

print_upper_words(words, must_start_with)