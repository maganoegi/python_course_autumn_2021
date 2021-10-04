


def sorting_algorithm(lst):
    """TODO: one-line description

    TODO: multi-line detailed description

    ARGS:
        TODO: argument description

    RETURNS:
        TODO: return description
    """
    return sorted(lst)

def strings_to_ints(lst):
    """TODO: one-line description

    TODO: multi-line detailed description

    ARGS:
        TODO: argument description

    RETURNS:
        TODO: return description
    
    RAISES:
        TODO: ValueError: description of the situation when it's raised
    """
    return list(map(lambda x : int(x), lst))

def string_to_strings(string):
    """TODO: one-line description

    TODO: multi-line detailed description

    ARGS:
        TODO: argument description

    RETURNS:
        TODO: return description
    """
    return string.split(",")



if __name__ == '__main__':

    input_string = input("Comma-separated numbers: ")

    list_of_strings = string_to_strings(input_string)
    
    list_of_ints = strings_to_ints(list_of_strings)
    
    sorted_list = sorting_algorithm(list_of_ints)
    
    print(sorted_list)