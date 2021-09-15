# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html

import string

shift = 3
choice = raw_input(r"would you like to encode or decode?")
word = (raw_input(r"Please enter text"))
letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]
        if choice == "decode":
            for letter in word:
                if letter == ' ':
                    encoded = encoded + ' '
                else:
                    x = letters.index(letter) - shift
                    encoded = encoded + letters[x]

print (encoded)

# pytest.py:25:7: E0001: Missing parentheses in call to 'print'. Did you mean print(encoded)? (<unknown>, line 25) (syntax-error)

