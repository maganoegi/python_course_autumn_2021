


def get_insertion_index(tree, value):
    pass

def add_to_tree(tree, value):
    tree = tree[:]
    

if __name__ == '__main__':
    tree = []
    done = False
    while not done:
        try:
            value = int(input("Integer to insert into the binary tree:\t"))
            tree = add_to_tree(tree, 2)
            print(tree)
        except:
            print("I TOLD YOU TO GIVE ME AN INTEGER!")

