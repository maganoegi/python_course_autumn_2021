
from typing import List

import std
import lib
import sys
import commands as cmds

def parse_words(words: List[str]) -> None:
    
    try:
        cnt = 0
        while cnt < len(words):
            increment_cnt = 1
            word = words[cnt]

            if word == "ls":
                is_list: bool = (
                    lib.index_exists(words, cnt + 1) and 
                    words[cnt + 1] == "-l"
                )

                increment_cnt = increment_cnt + 1 if is_list else increment_cnt

                contents = cmds.ls(is_list)

                std._out_ += contents

            elif word == "pwd":
                content = cmds.pwd()
                std._out_ += content

            elif word == "cd":
                # if no path -> print current directory
                if not lib.index_exists(words, cnt + 1):
                    std._out_ += cmds.pwd()
                else:
                    # normal cd navigation:
                    # .. for back ; name for folder
                    cmds.cd(words[cnt + 1])
                    increment_cnt += 1

            elif word == "mkdir":
                # mkdir [foldername1] [foldername2]...[foldernameN] -> creates the folder with the [foldername] 
                # check if the file/folder already exists for all of them.
                # else raise an error FileExistsError

                # import os.path
                # os.path.exists(file_path) # checks whether the path exists
                # os.path.isfile(file_path) #checks whether it's a directory
                pass

            elif word == "exit":
                sys.exit(0)
                print("Good Bye!")
                # exit -> exits the shell, displaying a goodbye message
                pass

            elif word == "touch":
                # touch [filename1] [filename2] ... [filenameN] -> creates those files
                # check if the file/folder already exists for all of them.
                # else raise an error FileExistsError
                pass

            else:
                raise lib.NotArgumentException

            cnt += increment_cnt


    except lib.NotArgumentException as e:
        std._err_ += "this argument does not exist:" + e.args[0]
    except FileNotFoundError:
        std._err_ += "file not found"
    except PermissionError:
        std._err_ += "you do not have permission to do that"
    except FileExistsError:
        std._err_ += "file with that name already exists"
    except NotADirectoryError:
        std._err_ += "the element is not a directory"
    except IsADirectoryError:
        std._err_ += "that element is a directory"
    except Exception as e:
        # general exception, for when all the others fail
        std._err_ += e.args[0]