


def bubble_sort(lst):
    """Applies a bubble sort algorithm to a list.

    Bubble sort is the simplest sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order. 

    No error handling is provided on this function - we assume that the input 
    is of the Integer type

    ARGS:
        A list to be sorted

    RETURNS:
        A sorted list
    """
    arr = lst[:]
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):

        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

def strings_to_ints(lst):
    """transforms a list of strings to a list of ints

    ARGS:
        list of strings

    RETURNS:
        list of ints
    
    RAISES:
        ValueError: when the string in the list is not a number
    """
    return [int(x.strip()) for x in lst]

def string_to_strings(string):
    """transforms a comma-separated string to a list of strings"""
    return string.split(",")



if __name__ == '__main__':

    input_string = input("Comma-separated numbers: ")

    list_of_strings = string_to_strings(input_string)
    
    list_of_ints = strings_to_ints(list_of_strings)
    
    sorted_list = bubble_sort(list_of_ints)
    
    print(sorted_list)