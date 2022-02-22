





WIDTH = 12

def func2(x, y, z):
    print(x + y + z)
    return y

def func(lst):
    lst.append(1)
    return lst



if __name__ == '__main__':

    lst = [1, 2, 3, 4, "5", 6, "sept", "8"]

    res = lst[::2][-2:][:-1] 

    print(res) 

