






if __name__ == '__main__':

    start_list = list(range(0, 10)) # 0-9
    print("start: ", start_list)

    sorted_list = sorted(start_list)
    print("sorted: ", sorted_list)

    squared_list = list(map(lambda x : x**2, start_list))
    print("squared: ", squared_list)

    only_bigger_than_5 = list(filter(lambda x : x > 5.0, start_list))
    print("bigger 5: ", only_bigger_than_5)

    combined_list = [
        start_list,
        sorted_list,
        squared_list,
        only_bigger_than_5
    ]
    print("combined: ", combined_list)

    total_sum = sum([sum(l) for l in combined_list])
    print("sum: ", total_sum) # -> 405
