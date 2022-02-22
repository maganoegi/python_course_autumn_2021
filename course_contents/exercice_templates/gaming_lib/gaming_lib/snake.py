

from gaming_lib.game import Game
import enum
from typing import List, Tuple
from collections import namedtuple

class InstructionSet(enum.Enum):
    UP=["k","w"]
    DOWN=["m","s"]
    LEFT=["j","a"]
    RIGHT=["l","d"]

class CellState( enum.Enum ):
    SNAKE = "s"
    APPLE = "a"
    EMPTY = " "

PositionCoords = namedtuple("PositionCoords", ["row", "col"])

grid_t = List[List[CellState]] # alias de type

class Snake( Game ):

    def __init__(self):
        ...

    def _create_row(self, width: int) -> List[CellState]:
        return [CellState.EMPTY.value for _ in range(width)]

    def _create_grid(self, width: int, height: int) -> grid_t:
        return [self._create_row(width) for _ in range(height)]

    def _initialize(self, width: int, height: int) -> grid_t:  
        self._done = False
        return self._create_grid(width, height)

    def _display(self, grid: grid_t) -> None:
        for row in grid:
            # res = [COL OPERATION for COL in COLLECTION if FILTER]
            res = "".join([
                "|" + (" " if col == None else str(col))     # OPERATION
                for col                         # DECLARATION
                in row                          # COLLECTION
                # if FILTER                     # CONDITION
            ]) + "|"
            print(res)

    def _get_instruction_from_user(self) -> InstructionSet:
        ...

    def _process(self, c_old, instruction: InstructionSet, grid: grid_t) -> grid_t:
        INSTRUCTION_COORDINATE_MAPPING = {
            InstructionSet.UP : (c_old.row-1, c_old.col),
            InstructionSet.DOWN : (c_old.row+1, c_old.col),
            InstructionSet.LEFT : (c_old.row, c_old.col-1),
            InstructionSet.RIGHT : (c_old.row, c_old.col+1),
        }
        return PositionCoords(*INSTRUCTION_COORDINATE_MAPPING[instruction])


    def _check_complete(self, grid: grid_t) -> bool:
        

    def play(self):
        WIDTH = 5
        HEIGHT = 5

        #initialiser un état de jeu
        self._grid, coords = self._initialize(width=WIDTH, height=HEIGHT)
        while not self.done:
            #presenter interface (affichage)
            self._display(self._grid, coords)

            # j left k up l right m down : instruction prompt()
            instruction = self._get_instruction_from_user()

            # process instructions
            self._grid, coords, statuses = self._process(coords, instruction,self._grid)

            #check done
            self.done=self._check_complete(statuses)
        
        # then prompt()


if __name__ == '__main__':
    ...        

