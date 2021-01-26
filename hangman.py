import random
import string
from hangman_photos import HANGMAN_PHOTOS

LOGO = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""

# print(LOGO)
# print(random.randint(5, 10))
# guess = input("Guess a letter:")
# print(("_ "*len(guess)).strip())  # Order of Operations / strips the last space


def punctuationInString(letter_guessed):
    for char in letter_guessed:
        if char in string.punctuation:
            return True
    return False


""" Conditions """
# if punctuationInString(guess) and len(guess) > 1:
#     print("E3")
# elif len(guess) > 1:
#     print("E1")
# elif punctuationInString(guess):
#     print("E2")
# else:
#     print(guess.lower())


""" Function """


def is_valid_input(letter_guessed):
    if punctuationInString(letter_guessed) and len(letter_guessed) > 1:
        return False
    elif len(letter_guessed) > 1:
        return False
    elif punctuationInString(letter_guessed):
        return False
    else:
        return True


# print(is_valid_input(guess))
""" Lists """
old_letters_guessed = []


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if is_valid_input(letter_guessed) and (letter_guessed not in old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print("->".join(sorted(old_letters_guessed)))
        return False


""" Loops """

# secret_word = "yes"
# old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']

# secret_word = "friends"
# old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']

word_guessed = []


def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char in old_letters_guessed:
            word_guessed.append(char)
    if len(secret_word) == len(word_guessed):
        return True
    return False


""" Data structures """


def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS[num_of_tries]
