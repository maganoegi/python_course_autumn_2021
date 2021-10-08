






if __name__ == '__main__':

    start_list = [34, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

    sorted_list = sorted(start_list)
    print("sorted: ", sorted_list)

    squared_list = [x**2 for x in start_list]
    print("squared: ", squared_list)

    only_negative = [x for x in start_list if x < 0.0]
    print("negative: ", only_negative)

    combined_list = [
        start_list,
        sorted_list,
        squared_list,
        only_negative
    ]
    print("combined: ", combined_list)

    total_sum = sum([sum(l) for l in combined_list])
    print("sum: ", total_sum)

    average_with_initial_len = total_sum / len(start_list)
    print("average: ", average_with_initial_len)

    rounded_down = int(average_with_initial_len)
    print("rounded: ", rounded_down) # -> 7324
