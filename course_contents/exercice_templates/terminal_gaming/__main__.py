
from termgamelib.factory import GameFactory

if __name__=='__main__':
    # game_name = input("Name of the game?\t")
    game = GameFactory.select_game("sudoku")
    game.play()

