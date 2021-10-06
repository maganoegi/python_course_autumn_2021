
import sys

def input_manager(default, args):
    """Handles the user input for this exercice.
    
    There are 2 use cases: 1) no input - use default. 2) phrase provided.

    ARGS:
        args tuple
    
    RETURNS:
        a single string
    """
    return default if len(args) == 1 else " ".join(args[1:])

def rotate_char(alphabet, rotate_by, character):
    c = character.lower()

    # Keep punctuation and whitespace
    # check whether the character is in alphabet
    if ...:
        return c

    # move the ord() number by 3 characters
    # NOTE: ord() gives the Unicode value of the character
    ...

    # If the rotation is inside the alphabet:
    if ...:
        # return the string that represents the unicode
        # NOTE: chr() gives a string from the unicode value
        return ...

    # If the rotation goes beyond the alphabet
    # substract the alphabet length from the unicode and make string
    return ...

if __name__ == '__main__':
    DEFAULT = "python can also be used for hacking"
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    ROTATION_NB = 3

    arguments = sys.argv

    message = input_manager(DEFAULT, arguments)

    encoded_msg = ... # something with rotate_char()...

    print(
        encoded_msg if len(arguments) > 1 
                    else encoded_msg == "sbwkrq fdq dovr eh xvhg iru kdfnlqj"
    )
