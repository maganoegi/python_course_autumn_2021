

from termgamelib.terminalgame import TerminalGame
import random
from typing import List

class Hangman( TerminalGame ):
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
        "python",
        "iterator",
        "generator",
        "mutability",
        "abstraction",
        "nomades",
        "classmethod"
    ]
    error_count = 0
    selected_word = random.choice(WORDS)
    current_progress = "_" * len(selected_word)
    nb_errors = len(HANGMAN_PICS)
    done = False

    @classmethod
    def display(cls) -> None:
        print(cls.HANGMAN_PICS[cls.error_count])
        print(cls.current_progress)


    @classmethod
    def open_underscores(
        cls, 
        hidden_string: str, 
        letter_occurences: List[int],
        user_input: str
    ) -> str:
        return "".join(
                    user_input if i in letter_occurences and c == "_" else c 
                    for i, c in enumerate(hidden_string)
                )


    @classmethod
    def play(cls) -> None:
        while not cls.done:
            cls.display()
            user_input = input("\nInput:\t")
            if len(user_input) != 1:
                print("Please provide a single value")
                continue

            if user_input in cls.selected_word and user_input not in cls.current_progress:
                # if the proposed letter is new
                occurences = [
                    i for i, c in enumerate(cls.selected_word) if c == user_input
                ]

                cls.current_progress = cls.open_underscores(
                    hidden_string=cls.current_progress,
                    letter_occurences=occurences,
                    user_input=user_input,
                )

                if cls.current_progress == cls.selected_word:
                    print("YOU WON!!!!!!")
                    print(f"Word: {cls.selected_word}")
                    cls.done = True
            
            elif user_input in cls.selected_word and user_input in cls.current_progress:
                # if the proposed letter has bee used already
                continue

            else:
                # if the proposed letter is not in the word
                cls.error_count += 1
                if cls.error_count == cls.nb_errors:
                    print("YOU LOST!!")
                    cls.done = True



if __name__ == '__main__':
    Hangman.play()




