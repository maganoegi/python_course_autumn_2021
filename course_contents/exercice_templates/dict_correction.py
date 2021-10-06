



def create_my_dict(*args):
    keys = []
    values = []
    for arg in args:
        key = arg[0]
        value = arg[1]

        if key in keys:
            key_index = keys.index(key)
            values[key_index] = value
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