

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

WORDS = [
    "chocolat", 
    "python",
    "plainpalais",
    "servette",
    "iterator",
    "generator",
    "mutability",
    "inheritance",
    "hangman",
    "nomades",
    "coffee"
]

import random

def main() -> None:
    selected_word = random.choice(WORDS)
    current_progress = "_" * len(selected_word)
    done = False

    while not done:
        print(current_progress)
        user_input = input("\nInput:\t")
        if len(user_input) != 1:
            print("Please provide a single value!!!!!!!!")
            continue

        # if the letter exists in word and not yet "opened"
            ...

        # elif the letter exists and has been opened already
            ...

        # else: NOTE: if the letter does not exist in word
            ...
            



if __name__ == '__main__':
    main()