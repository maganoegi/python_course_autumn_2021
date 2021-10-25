
import enum
import sys
from typing import List

class Flags( enum.Enum ):
    MANUAL = ("-m", "--manual")
    DOCUMENTATION = ("-d", "--doc")
    HELP = ("-h", "--help")

    def all_values():
        return [v for f in Flags for v in f.value]

    def contains_documentation_flags(args) -> bool:
        any(x in args for x in Flags.DOCUMENTATION.value)

def production_mode() -> None:
    print("Launching PROD Mode.....")

def debug_mode() -> None:
    print("Launching DEBUG Mode.....")

def generate_documentation() -> None:
    print("Generating Documentation......")

def argument_manager() -> None:
    HELP_TEXT = """
    CCHE Assistant API.
    Format: 'python3 . [-d][-m][-h]'
    -d, --doc\t\t: generate documentation using pdoc
    -m, --manual\t: launch manually, bypassing the flask server launche
    -h, --help\t\t: help menu
    """
    args = sys.argv
    if len(args) == 1:
        production_mode()

    else:
        # checks whether there are flags to work with...
        if any(x in args for x in Flags.all_values()):

            # checks if ANY flags are of the manual type...
            if any(x in args for x in Flags.MANUAL.value):
                debug_mode()
            else:
                production_mode()

            # checks if ANY flags are of the documentation type...
            if Flags.contains_documentation_flags(args):
                generate_documentation()

            # checks if ANY flags are of the help type...
            if any(x in args for x in Flags.HELP.value):
                print(HELP_TEXT)
        else:
            # if no useable flags are found
            print(HELP_TEXT)

if __name__ == '__main__':
    argument_manager()