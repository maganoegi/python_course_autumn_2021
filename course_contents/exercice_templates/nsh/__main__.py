
# built-in modules
import os
import sys

# custom modules
import std
import lib
import input_handler

PROMPT = "?>"

if __name__ == '__main__':
    
    # display welcome message
    lib.display_welcome_msg()

    # get current directory to store in the root, for reference
    std._root_ = os.getcwd()

    while True:
        #  reset std variables
        lib.reset_std()

        # gets the current directory for prompt purposes
        current_dir = os.getcwd()

        _input_ = input(current_dir + PROMPT)

        lines = lib.split_lines(_input_)

        for line in lines:
            words = line.split()

            input_handler.parse_words(words)

            lib.print_std()

