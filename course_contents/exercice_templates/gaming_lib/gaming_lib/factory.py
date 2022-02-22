


from gaming_lib.hangman import Hangman
# from gaming_lib.connect_four import ConnectFour
from gaming_lib.game import Game
from gaming_lib.snake import Snake

import gaming_lib.exceptions as exs

import enum


class GameNames( enum.Enum ):
    HANGMAN_NAMES = ["hangman", "pendu"]
    C4_NAMES = ["connect_four", "c4", "connectfour", "four"]
    SNAKE_NAMES = ["snake", "serpent"]

    def get_all_possible():
        return [word for row in GameNames for word in row.value]

def user_input_handler():
    res = None
    while res == None:
        try:
            word = input("what game would you like to play? ")
            if word not in GameNames.get_all_possible():
                raise exs.NotValidOptionException
            elif len(word) == 0:
                raise exs.EmptyUserEntryException
            else:
                res = word

        except exs.NotValidOptionException as e:
            print(e.prompt)
            continue

        except exs.EmptyUserEntryException:
            print("Please give us at least something......")
            continue

    return res

def get_game_from_string(input: str) -> Game:
    if input in GameNames.HANGMAN_NAMES.value:
        return Hangman()
    # elif input in GameNames.C4_NAMES.value:
    #     return ConnectFour()
    elif input in GameNames.SNAKE_NAMES.value:
        return Snake()

def execute_game(game) -> None:
    game.play()

def launch():
    game_name = user_input_handler()
    game = get_game_from_string(game_name)
    execute_game(game)


if __name__ == '__main__':
    ...