





if __name__ == '__main__':
    
    dataset = [
        [(66, "hdw"), (114, "rew"), (97, "lkj")],
        (("eew", "118", "rre"), ("asd", "111", "sda"), ("sdww", "32")), 
        "iuhiwen121asoicj",
        [111.0, 117.0, 32.2],
        {"a": 102, "b" : 111, "c" : 117},
        [{110, 100, 32}, {109, 101}]
    ]

    first = [x[0] for x in dataset[0]]
    print(first)

    second = [int(x[1]) for x in dataset[1]]
    print(second)

    third = [int(dataset[2][7:10])]
    print(third)

    fourth = [int(x) for x in dataset[3]]
    print(fourth)

    fifth = [int(x) for x in dataset[4].values()]
    print(fifth)

    sixth = [x for partial in dataset[5] for x in list(partial)[::-1]]
    print(sixth)

    together = [
        first, second, third, fourth, fifth, sixth
    ]
    print(together)

    as_strings = [chr(x) for partial in together for x in partial]
    print(as_strings)
    print("".join(as_strings))

