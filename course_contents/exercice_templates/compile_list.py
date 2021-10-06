

def combine_lists(*args):
    """Takes a variable number of lists and transforms them into one.
    
    ARGS:
        variable number of lists of different types
    
    RETURNS:
        a single list containing all of the elements from the collections.
    """
    return None

def flatten_list(*args):
    """Takes a variable number of lists and transforms them into one.
    
    Compared to combine_list(), this does it using a list comprehension.

    ARGS:
        variable number of lists of different types
    
    RETURNS:
        a single list containing all of the elements from the collections.
    """  
    return None

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    l3 = [11, 12, 13, 14]

    combined = combine_lists(l1, l2, l3)

    # flattened = flatten_list(l1, l2, l3)

    print(combined)
    # print(flattened)
    # print(combined == flattened)