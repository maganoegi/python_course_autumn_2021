



def create_my_dict(*args):
    keys = None
    values = None

    return keys, values

def display_my_dict(keys, values):
    print("TODO: print key and value pairs side by side")

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