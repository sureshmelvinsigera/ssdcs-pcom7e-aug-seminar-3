

"""
This script prompts a user to enter a message to encode or decode
"""

import string
from distlib.compat import raw_input

SHIFT = 3
choice = raw_input("would you like to encode or decode? ")
word = (raw_input("Please enter text "))
letters = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if choice == "encode":
    for i in word:
        if i == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = letters.index(i) + SHIFT
            ENCODED = ENCODED + letters[x]
        if choice == "decode":
            for letter in word:
                if letter == ' ':
                    ENCODED = ENCODED + ' '
                else:
                    x = letters.index(letter) - SHIFT
                    ENCODED = ENCODED + letters[x]

print(ENCODED)
