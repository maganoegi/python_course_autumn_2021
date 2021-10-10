
from typing import List

def calculate_pascal_triangle(n: int) -> List[int]:
    assert(n > 0, "N must be bigger than 0")
    lengths = [x + 1 for x in range(n)]
    lst = [1]
    if n in [1, 2]:
        return lst + [1, 1] * (n - 1)
    else:
        lst = []
        # lst = [1, 1, 1]
        # for l in lengths[2:]:
        #     regression = l - 1
        #     el = lst[]

    # mypy

def print_pascal(lst: List[int]) -> None:
    pass

def user_input_handler() -> int:
    done = False
    n = None
    while not done:
        try:
            n = int(input("Please provide an integer value:\t"))
            done = True
        except ValueError:
            print("I TOLD YOU I WANTED AN INTEGER!!!!")

    return n

if __name__=='__main__':
    n = user_input_handler()
    lst = calculate_pascal_triangle(n)
    print_pascal(lst)