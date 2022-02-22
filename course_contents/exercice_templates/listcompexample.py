




def get_only_even_from(lst):
    """ create a new list from an old one containing only the even numbers.

    ARGS:
        a list containing numerical values

    RETURNS:
        a list containing numerical values
    """
    new_list = []
    for val in lst:
        if val % 2 == 0:
            new_list.append(val)

    return new_list

def get_only_even_comprehension(lst):
    # [ x for x in collection if condition ]
    return [val for val in [x for x in lst] if val % 2 == 0]

def get_even_squared(lst):
    new_lst = []
    for val in lst:
        if val % 2 == 0:
            new_lst.append(pow(val, 2))
    return new_lst

def get_even_squared_comp(lst):
    return [item**2 for item in lst if item in shoppingcart]

    return map(lambda x : x**2, filter(lambda x : x % 2 == 0))


def get_even_matrix(matrix):
    new_lst = []
    for x in matrix:
        for val in x:
            if val % 2 == 0:
                new_lst.append(val)

    return new_lst

def get_even_squared_comp_from_matrix(matrix):
    return [val for lst in matrix for val in lst if val % 2 == 0 or val == 3]

def exercice_1(fruits, numbers):
    fruits_upper_simple = [val.upper() for val in fruits]
    print(fruits_upper_simple)

def exercice_2(fruits, numbers):
    # ['Mango', 'Kiwi', 'Strawberry', etc...]
    fruits_upper_capitalized = [[char.upper() if string.index(char) == 0 else char for char in string] for string in fruits]
    fruits_upper_capitalized = [val.capitalize() for val in fruits]
    print(fruits_upper_capitalized)

def exercice_3(fruits, numbers):
    # make a list that contains each fruit with more than 5 characters
    fruits_longer_than_5 = [fruitstring for fruitstring in fruits if len(fruitstring) > 5]

def exercice_4(fruits, numbers):
    # make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
    char_count_lst = [len(string) for string in fruits]

def exercice_5(fruits, numbers):
    # Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
    with_a = [string for string in fruits if "a" in string]

def exercice_6(fruits, numbers):
    # [operation - declaration - collection - condition]
    even_numbers_plus_1 = [number + 1 for number in numbers if number % 2 == 0]

def exercice_7(fruits, numbers):
    # Make a variable named positive_numbers that holds only the positive numbers, 0 included
    only_positive = [number for number in numbers if number >= 0]



if __name__ == '__main__':
    
    # lst = [1, 2, 3, 4, 5, 6, 896, 11]

    # even_lst = get_only_even_comprehension(lst)

    # even_lst_squared = get_even_squared(lst)

    # print(lst, id(lst))
    # print(even_lst, id(even_lst))
    # print(even_lst_squared, id(even_lst_squared))

    # matrix = [
    #     [1, 2, 3, 4, 5],
    #     [1, 2, 30, 4, 50],
    #     [1, 2, 30, 4, 50],
    #     [1, 2, 30, 4, 50],
    #     [1, 2, 30, 4, 50],
    #     [1, 2, 30, 4, 50],
    # ]

    # even_matrix = get_even_matrix(matrix)
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
    exercice(fruits, numbers)









