import random
import string
import os
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


""" Conditions and Function """


def is_valid_input(letter_guessed):
    if punctuationInString(letter_guessed) and len(letter_guessed) > 1:
        return False
    elif len(letter_guessed) > 1:
        return False
    elif punctuationInString(letter_guessed):
        return False
    else:
        return True


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


""" Files """
words = "words.txt"
script_dir = os.path.dirname(__file__)
file_path = f"{script_dir}\{words}"


def choose_word(file_path, index):
    with open(file_path, "r") as f:
        words = f.read()
        splitted = words.split()
        mod = index % len(splitted)
        if mod > 0:
            return len(set(splitted)), splitted[mod-1]
        return len(set(splitted)), splitted[index-1]
