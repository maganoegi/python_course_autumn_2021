





if __name__ == '__main__':
    
    dataset = [
        [(66, "hdw"), (114, "rew"), (97, "lkj")],
        (("eew", "118", "rre"), ("asd", "111", "sda"), ("sdww", "32")), 
        "iuhiwen121asoicj",
        [111.0, 117.0, 32.2],
        {"a": 102, "b" : 111, "c" : 117},
        [{110, 100, 32}, {109, 101}]
    ]

    first = ...
    print(first)

    # take the numerical data out and transform to int
    second = ...
    print(second)

    # take the numerical data out and transform to int
    third = ...
    print(third)

    # take the float data out and transform to int
    fourth = ...
    print(fourth)

    fifth = ...
    print(fifth)

    sixth = ...
    print(sixth)

    together = [
        first, second, third, fourth, fifth, sixth
    ]
    print(together)

    as_strings = [chr(x) for partial in together for x in partial]
    print(as_strings)
    print("".join(as_strings))

