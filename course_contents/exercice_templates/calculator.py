
from typing import Callable, List # importer qqchose de particulier
# import typing # importer le module en entier

def ask_user_int(prompt: str) -> int:
    result = None
    while result == None:
        try:
            result = int(input(prompt))

        except ValueError: # catch en JS
            print("Please provide an integer value")
            continue

    return result

def ask_user_op(prompt: str) -> str:
    result = None # null / undefined en JS

    while not result: # False, None, 0, "", []
        raw = input(prompt)
        if raw in ["*", "//", "-", "+", "/", "%"]:
            result = raw
        else:
            print("Please select from the following values: \* / // % + -")
            continue

    return result

def multiplication(x, y):
    return x * y

def select_operation(operation_string: str) -> Callable: # mypy
    if operation_string == "*":
        return lambda x, y : x * y 
        # return multiplication

    elif operation_string == "//":
        return lambda x, y: x // y
    
    elif operation_string == "-":
        return lambda x, y: x - y 

    elif operation_string == "+":
        return lambda x, y: x + y 
    
    elif operation_string == "/":
        return lambda x, y: x / y
    
    elif operation_string == "%":
        return lambda x, y: x % y 



def calculator():
    left = ask_user_int("Please provide a number\t")
    operation_string = ask_user_op("What's is the operation you would like to perform?\t")
    right = ask_user_int("Please provide a second number\t")
    
    operation = select_operation(operation_string)

    try:
        result = operation(left, right)
    except ZeroDivisionError:
        print("please don't divide by zero...") 
        exit(1)

    print(f"{left} {operation_string} {right} = {result}")


if __name__ == '__main__':
    # il faut coder pour l'interface et non pas pour l'implementation
    
    calculator()

    # pass
    # ...
    # raise NotImplementedError