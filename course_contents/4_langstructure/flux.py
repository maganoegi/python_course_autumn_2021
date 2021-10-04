
def scream_the_type(number):
    this_type = type(number)
    if this_type == int:
        print("THIS IS AN INT!!!")
    
    elif this_type == float:
        print("THIS IS A FLOAT")

    else:
        print("This is some other type.... might be a string?")

>>> scream_the_type("this is not a number")
"This is some other type.... might be a string?"

>>> x = 0
>>> result = []
>>> while x != 10:
...     result.append(x)
...     x += 1

>>> print(result)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# pattern que l'on trouve dans du code materiel...
while True:
    # do something
    if stop_condition:
        break



# pattern que l'on trouve dans du code analytique...
while condition:

    if do_condition:
        # do something

    elif skip_condition:
        continue

    elif stop_condition:
        break

    else:
        pass # do NOTHING



# boucle FOR - (quand nombre iterations connu)...

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# parcourir une liste en longueur...
for i in range(len(lst)):
    print(lst[i])

# range donne un ITERATEUR de 0 à 9 
# mais vu que LIST est deja un ITERABLE... 

# parcourir la liste par valeur...
for value in lst:
    print(value)


# parcourir la liste avec indice et valeur...
for i, value in enumerate(lst):
    print(f"value {value} at index {i}")

