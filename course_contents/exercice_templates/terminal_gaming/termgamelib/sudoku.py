
from termgamelib.terminalgame import TerminalGame
from typing import Tuple, Optional, List
import random
grid_t = List[List[Optional[int]]]



# class Grid:
#     def __init__(self, content):
#         self._content = content
    
#     @property
#     def content(self):
#         return self._content

#     def get_row_values(self, row: int):
#         return [sg for sg in self.content]

# class SubGrid:
#     def __init__(self, content):
#         self._content = content
    
#     @property
#     def content(self):
#         return self._content

#     def get_row_values(self, row: int):
#         return [val for val in self.content[row]]

# class Box:
#     def __init__(self, value: Optional[int] = None):
#         self._value = value

#     @property
#     def content(self):
#         return self._value










class Sudoku( TerminalGame ):

    DEFAULT_DIM = 9
    grid = None
    done = False

    @classmethod
    def display(cls):
        for row in cls.grid:
            print(" ".join(str(val) if val != None else "." for val in row))

    @classmethod
    def _init_grid(cls, grid: grid_t, level: int = 1) -> grid_t:
        grid = [[None for _ in range(cls.DEFAULT_DIM)] for _ in range(cls.DEFAULT_DIM)]
        nb_operations = cls.DEFAULT_DIM - level * 2
        for i in range(cls.DEFAULT_DIM):

            for _ in range(nb_operations):
                success = False
                while not success:
                    value = random.randint(1, cls.DEFAULT_DIM)
                    col = random.randint(0, cls.DEFAULT_DIM-1)
                    is_possible = cls._check_if_insert_possible(grid, i, col, value) 
                    if is_possible:
                        grid = cls._insert_into_grid(grid, i, col, value)
                        success = True

        return grid

    @classmethod
    def _get_user_input(cls) -> Tuple[int, int, int]:
        row = int(input("row ")) - 1
        col = int(input("col ")) - 1
        value = int(input("value "))
        return row, col, value

    @classmethod
    def _check_row_validity(
        cls, 
        grid: grid_t, 
        row: int, 
        value: int
    ) -> bool:
        return value not in grid[row]

    @classmethod
    def _check_col_validity(
        cls, 
        grid: grid_t, 
        row: int, 
        col: int, 
        value: int
    ) -> bool:
        return value not in [grid[i][col] for i in range(len(grid))]

    @classmethod
    def _check_submatrix_validity(
        cls, 
        grid: grid_t, 
        row: int, 
        col: int, 
        value: int
    ) -> bool:
        # TODO: implement _check_submatrix_validity
        return True

    @classmethod
    def _check_if_insert_possible(
        cls, 
        grid: grid_t, 
        row: int, 
        col: int, 
        value: int
    ) -> bool:
        row_valid = cls._check_row_validity(grid, row, value)
        col_valid = cls._check_col_validity(grid, row, col, value)
        submatrix_valid = cls._check_submatrix_validity(grid, row, col, value)

        return row_valid and col_valid and submatrix_valid

    @classmethod
    def _insert_into_grid(
        cls, 
        grid: grid_t, 
        row: int, 
        col: int, 
        value: int
    ) -> grid_t:
        new_grid = grid[:]
        new_grid[row][col] = value
        return new_grid

    @classmethod
    def play(cls):
        cls.grid = cls._init_grid(cls.grid)

        while not cls.done:
            cls.display()

            row, col, value = cls._get_user_input()

            can_be_inserted = cls._check_if_insert_possible(
                                                            cls.grid, 
                                                            row, 
                                                            col, 
                                                            value
                                                            )
            
            if can_be_inserted:
                cls.grid = cls._insert_into_grid(cls.grid, row, col, value)
            else:
                print("NOOOOOOPOOOOOOASIOPSKFHFL")





