

import random
from typing import List
from gaming_lib.game import Game

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

class Hangman( Game ):
    WORDS = [
        "python",
        "iterator",
        "generator",
        "mutability",
        "abstraction",
        "nomades",
        "classmethod"
    ]

    def __init__(self, word: str = None):
        self._word = self._select_word(word)
        self._done = True

    @property
    def word(self) -> str:
        return self._word

    @property
    def is_running(self) -> bool:
        return not self._done

    def _select_word(self, word) -> None:
        """ instance method allowing for word attribution """
        return word if word != None else random.choice(self.WORDS)

    def _display(self, image: str, progress: str) -> None:
        print(image)
        print(progress)

    @classmethod
    def _get_letter_occurences(cls, word: str, letter: str) -> List[int]: 
        """Get all the index occurences of a given letter in a string.
        
        For a given word, look at all of the letters and filter out the indices
        of occurence of that particular letter, putting them in a list.

        ARGS:
            word: str : the reference word to be checked.
            letter : str: letter, occurences of which need to be found in word.
        
        RETURNS:
            list[int] : the indices organized in a list.
        
        """
        return [i for i, c in enumerate(word) if c == letter]

    @classmethod
    def _update_current_progress(
        cls, 
        current_progress: str, 
        occurences: List[int], 
        user_input: str
    ) -> str:
        return "".join(
            user_input if i in occurences and c == "_" else c 
            for i, c in enumerate(current_progress)
        )

    def _display_winner(self):
        print("YOU WON!!!!!!")
        print(f"Word: {self.word}")

    def _check_for_winner(self, progress: str, word: str) -> bool:
        done = False
        if progress == word:
            self._display_winner()
            done = True
        return done

    def play(self):
        self._done = False
        selected_word = self.word
        current_progress = "_" * len(selected_word)
        nb_errors = len(HANGMAN_PICS)
        error_count = 0

        while self.is_running:
            self._display(HANGMAN_PICS[error_count], current_progress)
            user_input = input("\nInput:\t")
            if len(user_input) != 1:
                print("Please provide a single value")
                continue

            if (user_input in selected_word and 
                user_input not in current_progress):
                occurences = self.__class__._get_letter_occurences(
                    selected_word, 
                    user_input
                )
                current_progress = self._update_current_progress(
                    current_progress, 
                    occurences, 
                    user_input
                )
                self._done = self._check_for_winner(
                    current_progress, 
                    selected_word
                )

            elif user_input in selected_word and user_input in current_progress:
                continue

            else:
                error_count += 1
                if error_count == nb_errors:
                    print("YOU LOST!!")
                    self._done = True

if __name__ == '__main__':
    Hangman().play()