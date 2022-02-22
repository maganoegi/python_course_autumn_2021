






if __name__ == '__main__':

    start_list = [34, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

    sorted_list_ascending = sorted(start_list)
    print("sorted: ", sorted_list_ascending)

    sorted_list_descending = sorted(start_list, reverse=True)
    sorted_list_descending = sorted(start_list)[::-1]
    print("sorted: ", sorted_list_descending)


    squared_list = [nb**2 for nb in start_list]
    squared_list = [pow(nb, 2) for nb in start_list]
    print("squared: ", squared_list)

    only_negative = [number for number in start_list if number < 0]
    print("negative: ", only_negative)

    combined_list = [
        start_list,
        sorted_list_ascending,
        squared_list,
        only_negative
    ]
    print("combined: ", combined_list)

    total_sum = sum([sum(lst) for lst in combined_list])
    total_sum = sum([item for lst in combined_list for item in lst]) # flatten the matrix
    print("sum: ", total_sum)

    average_with_initial_len = total_sum / len(start_list)
    print("average: ", average_with_initial_len)

    rounded_down = int(average_with_initial_len)
    print("rounded: ", rounded_down) # -> 7384
