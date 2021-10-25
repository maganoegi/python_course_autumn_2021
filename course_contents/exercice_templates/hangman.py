

HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ==='''
]

import random

WORDS = [
    "python",
    "iterator",
    "generator",
    "mutability",
    "abstraction",
    "nomades",
    "classmethod"
]

def main():
    done = False
    selected_word = random.choice(WORDS)
    current_progress = "_" * len(selected_word)
    nb_errors = len(HANGMAN_PICS)
    error_count = 0

    while not done:
        print(HANGMAN_PICS[error_count])
        print(current_progress)
        user_input = input("\nInput:\t")
        if len(user_input) != 1:
            print("Please provide a single value")
            continue

        if user_input in selected_word and user_input not in current_progress:
            # if the proposed letter is new
            occurences = ... # TODO

            current_progress = ... # TODO

            if current_progress == selected_word:
                print("YOU WON!!!!!!")
                done = True
        
        elif user_input in selected_word and user_input in current_progress:
            # if the proposed letter has bee used already
            continue

        else:
            # if the proposed letter is not in the word
            error_count += 1
            if error_count == nb_errors:
                print("YOU LOST!!")
                done = True


if __name__ == '__main__':
    main()