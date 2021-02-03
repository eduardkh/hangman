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
file_path = input("Enter file path: ")
index = input("Enter index: ")

print(file_path)
print(index)
