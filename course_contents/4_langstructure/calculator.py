



def ask_user_int(prompt):
    result = None
    while not result:
        try:
            result = int(input(prompt))

        except:
            print("Please provide an integer value")
            continue
    
    return result

def ask_user_op(prompt):
    result = None
    while not result:
        raw = input(prompt)
        if raw in ["*", "//", "-", "+", "/", "%"]:
            result = raw
        else:
            print("Please select from the following values: \
                    * / // % + -")
            continue

    return result

def select_operation(op_str):
    if op_str == "*":
        return lambda x, y : x * y

    elif op_str == "/":
        return lambda x, y : x / y

    elif op_str == "//":
        return lambda x, y : x // y

    elif op_str == "-":
        return lambda x, y : x - y

    elif op_str == "+":
        return lambda x, y : x + y

    else:
        return lambda x, y : x % y

if __name__ == '__main__':
    left = ask_user_int("First Number: ")
    op_str = ask_user_op("Operation: ")
    right = ask_user_int("Second Number: ")
    
    operation = select_operation(op_str)

    result = operation(left, right)

    print(f"{left} {op_str} {right} = {result}")