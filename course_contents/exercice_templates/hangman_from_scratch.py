
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

def hangman() -> None:
    selected_word = random.choice(WORDS)
    current_progress = "_" * len(selected_word)
    done = False
    error_counter = 0

    while not done:
        print(HANGMAN_PICS[error_counter])
        print(current_progress)
        user_input = input("\nInput:\t")
        if len(user_input) != 1:
            print("Please provide a single value!!!!!!!!")
            continue

        if user_input in selected_word and user_input not in current_progress:
            # for i in range(len(current_progress)): index
            # for value in current_progress: value
            for i, value in enumerate(selected_word): # both
                if value == user_input:
                    current_progress = current_progress[:i] + user_input + current_progress[i+1:]

            # AUTRE MANIERE DE FAIRE
            # occurences = [
            #     i for i, c in enumerate(selected_word) if c == user_input
            # ]
            # current_progress = [
            #     c if i in occurences else current_progress[i] 
            #     for i, c in enumerate(selected_word)
            # ]
            
            if selected_word == current_progress:
                print("YOU WIN")
                done = True

                # reset logic
                selected_word = random.choice(WORDS)
                current_progress = "_" * len(selected_word)
                error_counter = 0
                continue

        elif user_input in selected_word and user_input in current_progress:
            continue

        else:
            error_counter += 1
            if error_counter == len(HANGMAN_PICS):
                print("YOU LOST")
                done = True

def main(game_function) -> None: # strategy design pattern
    game_function()
            
if __name__ == '__main__':
    main(hangman)