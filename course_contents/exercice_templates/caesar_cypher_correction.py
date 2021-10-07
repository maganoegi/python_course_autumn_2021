
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
    if c not in alphabet:
        return c

    # NOTE: ord() gives the Unicode value of the character
    rotated_pos = ord(c) + rotate_by

    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        # NOTE: chr() gives a string from the unicode value
        return chr(rotated_pos)

    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

if __name__ == '__main__':
    DEFAULT = "python can also be used for hacking"
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    ROTATION_NB = 3

    arguments = sys.argv

    message = input_manager(DEFAULT, arguments)

    encoded_msg = "".join([rotate_char(
        alphabet=ALPHABET,
        character=c,
        rotate_by=ROTATION_NB
    ) for c in message])
    
    print(
        encoded_msg if len(arguments) > 1 
                    else encoded_msg == "sbwkrq fdq dovr eh xvhg iru kdfnlqj"
    )
