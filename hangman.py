import random
import string


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

print(LOGO)
print(random.randint(5, 10))
guess = input("Guess a letter:")
print(("_ "*len(guess)).strip())  # Order of Operations / strips the last space


def punctuationInString(guess):
    for char in guess:
        if char in string.punctuation:
            return True
    return False


if punctuationInString(guess) and len(guess) > 1:
    print("E3")
elif len(guess) > 1:
    print("E1")
elif punctuationInString(guess):
    print("E2")
else:
    print(guess.lower())
