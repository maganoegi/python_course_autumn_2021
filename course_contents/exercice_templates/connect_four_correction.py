
import enum
import random
from typing import List

class SectionState( enum.Enum ):
    YELLOW = "💩"
    RED = "💥"
    EMPTY = "_"


class Player( enum.Enum ):
    ONE = enum.auto()
    TWO = enum.auto()


PLAYER_COLOR = {
    Player.ONE : SectionState.YELLOW,
    Player.TWO : SectionState.RED
}

matrix_t = List[List[SectionState]]

def display_matrix(m) -> None:
    for row in m:
        print(" ".join(val.value for val in row))

    print(" ".join(str(val) for val in range(1, len(m[0]) + 1)))

def insert_into_matrix(
    matrix: matrix_t,
    col: int,
    state: SectionState
) -> matrix_t:

    col_values = [matrix[i][col] for i in range(len(matrix))]
    if col_values[0] != SectionState.EMPTY:
        # if the column is full...
        pass

    else:
        last_free_index = col_values.count(SectionState.EMPTY) - 1
        matrix[last_free_index][col] = state
        
    return matrix


def connect_four(width: int = 7, height: int = 6, to_win: int = 4) -> None:
    done = False
    current_player = random.choice([p for p in Player])
    print(f"Current Player is: {current_player.name}")
    matrix = [[SectionState.EMPTY] * width] * height

    while not done:
        display_matrix(matrix)

        selected_column = int(input("column:\t"))
        if selected_column < 1 or selected_column > width:
            print("Gerard Depardieu rage car tu le mets a coté!!!!!")
            continue

        matrix = insert_into_matrix(
            matrix, 
            selected_column-1, 
            PLAYER_COLOR[current_player]
        )
        
        current_player = (Player.ONE if current_player == Player.TWO 
                                    else Player.TWO)
                                    

        


if __name__ == '__main__':
    connect_four()





