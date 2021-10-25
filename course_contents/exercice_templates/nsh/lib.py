
import std

from typing import List, TypeVar

T = TypeVar("T")

class NotArgumentException( Exception ):
    """ raised when an argument provided is not valid argument in our shell """
    pass

def split_lines(line: str) -> List[str]:
    lines = line.split(";")
    return lines

def print_std() -> None:
    # NOTE: we dont care about std.in here.....
    if std._err_ != "":
        print(std._err_)
    else:
        if std._out_ != "":
            print(std._out_)
        
        else:
            pass

def display_welcome_msg() -> None:
    print("Welcome to Nomades Shell !!!")

def index_exists(lst: List[T], index:int) -> bool:
    return -len(lst) <= index < len(lst)

def reset_std() -> None:
    std._out_ = ""
    std._in_ = ""
    std._err_ = ""