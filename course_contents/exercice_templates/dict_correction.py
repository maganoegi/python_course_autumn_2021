



def create_my_dict(*args):
    keys = []
    values = []
    for i, (key, value) in enumerate(args):

        if key in keys:
            values[i] = value
        else:
            keys.append(key)
            values.append(value)

    return keys, values

def display_my_dict(keys, values):
    print(f"my_dict: {list(zip(keys, values))}")

if __name__ == '__main__':

    kv_pairs = [
        ("a", 1),
        ("b", 2),
        ("c", 3),
        ("c", 4),
        ("b", 1),
    ]

    keys, values = create_my_dict(*kv_pairs)

    display_my_dict(keys, values)