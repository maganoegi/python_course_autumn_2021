

from termgamelib.terminalgame import TerminalGame
from termgamelib.hangman import Hangman
from termgamelib.connectfour import ConnectFour
from termgamelib.sudoku import Sudoku


class GameFactory:
    INPUT_GAME_MAPPING = {
        "hangman" : Hangman,
        "connectfour" : ConnectFour,
        "sudoku" : Sudoku
    }

    @classmethod
    def _clean_input(cls, msg) -> str:
        return msg.lower()

    @classmethod
    def select_game(cls, selection: str) -> TerminalGame:
        """Factory method that takes the user input, returns the TerminalGame"""
        selection = cls._clean_input(selection)

        if selection in cls.INPUT_GAME_MAPPING.keys():
            return cls.INPUT_GAME_MAPPING[selection]
        
        else:
            print("The game name you entered does not exist.")
            print("The following game names exist:")
            for k in cls.INPUT_GAME_MAPPING.keys():
                print(f"\t- {k}")
        