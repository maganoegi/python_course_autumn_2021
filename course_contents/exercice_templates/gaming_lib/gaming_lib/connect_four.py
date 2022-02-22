


# from typing import List, Optional

# from gaming_lib.game import Game

# class ConnectFour( Game ):
#     def play(self):
#         print()






# class InvalidColumnException( Exception ):
#     pass

# # def _get_user_col_number(grid) -> int:
# #     result = None
# #     nb_of_columns = len(grid[0])
# #     while result == None:
# #         try:
# #             uinput = int(input("Which column?\t"))
# #             if 1 <= uinput <= nb_of_columns:
# #                 result = uinput
# #             else:
# #                 raise InvalidColumnException

# #         except ValueError:
# #             print("please provide an integer value")
            
# #         except InvalidColumnException:
# #             print("invalid column number")

# #         finally:
# #             continue

# #     return result

# # def _display_grid(grid):
# #     for row in grid:
# #         # res = [COL OPERATION for COL in COLLECTION if FILTER]
# #         res = "".join([
# #             "|" + (" " if col == None else str(col))     # OPERATION
# #             for col                         # DECLARATION
# #             in row                          # COLLECTION
# #             # if FILTER                     # CONDITION
# #         ]) + "|"
# #         print(res)

# # def _display_player(current_player: int):
# #     print(f"current player is {current_player}")

# # def _create_row(width: int):
# #     return [None for _ in range(width)]

# # def _create_grid(width: int, height: int) -> List[List[Optional[int]]]:
# #     return [create_row(width) for _ in range(height)]

# # def _check_line(lst: List[int], needed: int) -> bool:
# #     return len(lst) >= needed

# # def _build_consecutive_for_player(line, col_nb, value):
# #     partial = []
# #     for i, v in enumerate(line):
# #         if line[i] == value:
# #             partial.append(v)
# #         else:
# #             break
    
# #     return partial

# # def _check_if_won(grid, current_player, col_nb, row_nb, needed: int):
# #     col_nb -= 1
    
# #     center = [current_player]

# #     horizontal_line = [grid[row_nb][i] for i in range(len(grid[row_nb]))] # -> width
# #     left = list(reversed(horizontal_line[:col_nb]))
# #     right = horizontal_line[col_nb+1:]
# #     left_horizontal = build_consecutive_for_player(left, col_nb, current_player)
# #     right_horizontal = build_consecutive_for_player(right, col_nb, current_player)

# #     target_horizontal = left_horizontal + center + right_horizontal
# #     h = check_line(target_horizontal, needed)
    
   
# #     vertical_line = [grid[i][col_nb] for i in range(len(grid))] # -> height
# #     bottom = vertical_line[row_nb+1:]
# #     bottom_vertical = build_consecutive_for_player(bottom, row_nb, current_player)
# #     target_vertical = center + bottom_vertical
# #     v = check_line(target_vertical, needed)

# #     # dr_line = [r+c for r, c in zip(range(col_nb-needed,col_nb+needed,-1))] 
# #     drt_line = [(r, c) for r, c in zip(range(row_nb, 0, -1), range(col_nb, len(grid[row_nb])))] 
# #     drb_line = [(r, c) for r, c in zip(range(row_nb, len(grid)), range(col_nb, 0, -1))] 

# #     # target_dr = diagonal_bottom_left + center + diagonal_top_right
# #     print(drt_line)
# #     print(drb_line)
# #     # dr = check_line(..., needed)
# #     # dl = check_line(..., needed)



# #     return h or v
# #     # return h or v or dr or dl
# #     # return any([h, v, dr, dl])

# # def _insert_at_column_into_grid(current_player: int, col_nb: int, grid):
# #     col = col_nb - 1
# #     height = len(grid)
# #     column = [grid[i][col] for i in range(height)]
# #     nb_of_empty = column.count(None)
# #     nb_of_empty = len([x for x in column if x == None])

# #     if nb_of_empty != 0:
# #         top_row = nb_of_empty - 1
# #         grid[top_row][col] = current_player

# #     return grid, nb_of_empty - 1

# # def play():
# #     print()
#     # NB_PLAYERS = 2
#     # WIDTH = 7
#     # HEIGHT = 6
#     # NEEDED = 4
#     # current_player = 0
#     # grid = _create_grid(WIDTH, HEIGHT)
#     # done = False
    
#     # while not done:
#     #     display_grid(grid)
#     #     display_player(current_player)

#     #     col_nb = get_user_col_number(grid)

#     #     grid, row_nb = insert_at_column_into_grid(current_player, col_nb, grid)

#     #     done = check_if_won(grid, current_player, col_nb, row_nb, NEEDED)
    
#     # _display_grid(grid)

# if __name__ == '__main__':
#     play()