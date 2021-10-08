

def exercise_1():
    """exercise that returns list of integers [1:1000) divisible by 8
    
    ARGS: 
        None

    RETURNS:
        list of integers [1:1000) divisible by 8
    """
    collection = range(1, 1001)
    filtered = filter(
        lambda individual_value : individual_value % 8 == 0, 
        collection
    )
    return list(filtered)

def exercise_2():
    """exercise that returns list of integers [1:1000) that has '6' in them.

    ARGS: 
        None

    RETURNS:
        list of integers [1:1000) that has '6' in them.
    """
    SIX = '6'
    r = range(1, 1001)
    return [val for val in r if SIX in str(val)]
    # return list(filter(lambda val : SIX in str(val), r))

def exercise_3(string):
    """counts the number of spaces in a given input string.

    ARGS: 
        a string

    RETURNS:
        an integer value representing the number of strings
    """
    SPACE = " "
    return string.count(" ")

def exercise_4(string):
    """TODO: 

    ARGS: 
        TODO:
    RETURNS:
        TODO:
    """
    VOWELS = "ayeuio"
    return "".join([c for c in string if c in VOWELS])

def exercise_5(string):
    """returns a list of words that have the length less than 5.

    ARGS: 
        TODO:
    RETURNS:
        TODO:
    """
    pass

if __name__ == '__main__':
    ex1 = exercise_1()

    ex2 = exercise_2()

    input_string = "nous apprenons Python"
    ex3 = exercise_3(input_string)

    input_string = "nous apprenons Python"
    output_string = exercise_4(input_string)

    input_string = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam placerat vestibulum gravida. Morbi ac risus eget justo porttitor porttitor at laoreet purus. Sed vitae sem id felis mattis ullamcorper. Sed feugiat eros non enim consequat mollis. Duis mollis pellentesque felis, in blandit ligula. Quisque quis elit luctus, hendrerit lorem a, pellentesque nisi. In hac habitasse platea dictumst. Ut blandit ac ex non tempor. Mauris placerat metus sem, ut interdum lorem tincidunt at. Etiam malesuada massa risus, in eleifend mauris accumsan iaculis. In hac habitasse platea dictumst. Vivamus quam est, semper vel dolor in, posuere consequat neque. """
    small_words = exercise_5(input_string)
    print(small_words)
