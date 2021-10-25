
import os

def ls(is_list: bool) -> str:
    """ fetches the contents of directory as a single line.
    
    FLAGS:
        is_list: generates the output string in a form of a list
    """
    content = os.listdir()
    separator = "\n" if is_list else " "
    return separator.join(content)

def pwd() -> str:
    return os.getcwd()

def cd(path: str) -> None:
    os.chdir(path)