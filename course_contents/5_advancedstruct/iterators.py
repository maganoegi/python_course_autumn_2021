
# pour des raisons de memoire et performance
# certaines fonctions retournent des ITERATEURS...

# appliquer my_func à chaque element dans la collection..
>>> map(my_func, [0, 1, 2, 3])
map object

# avoir un iterateur de 0 à 9...
>>> range(10)
range object

# filtrer les valeurs dans une collection...
>>> filter(lambda x : x % 2 == 0, [0, 1, 2, 3, 4, 5])
filter object

# Ces elements-là sont des iterateurs intermediaires
# qui nous permettent de les utiliser par la suite
#  et enchainer des operations...

# Enchainement: 
map(operation, iterator1, ..., iteratorN) -> iterator

>>> r = reversed(0, 1, 2, 3, 4)
>>> m = map(pow, r, range(10))
>>> list(m)
[1, 3, 4, 1, 0]


# EXEMPLE:
>>> def myfunc(a, b):
...     return a + b

>>> m = map(myfunc, [0, 1, 2, 3])
>>> # PAS D'ERREUR!
>>> list(m)
TypeError: missing 1 required positional argument 'b'

# Donc on voit que MAP effectue uniquement les liens
# en preparant le contenu à la sortie...
# ceci est la definition d'un iterateur

# Le mapping devient "concret", quand:
>>> list(m)
# OU
>>> m.__next__()

# Les itérateurs importants:
map(func, *collections)
reversed(collection)
zip(*collections)
filter(predicate, collection)

# comme c'est des "recettes", on ne peut pas les
# comparer directement... il faut de la logique en plus 

# par contre, quand on parcours un objet MAP
# on ne pourra plus l'utiliser...
>>> lst = [0, -1, -2, -3, -4]
>>> m = map(lambda x : abs(x), lst)
>>> list(m)
[0, 1, 2, 3, 4]
>>> list(m)
[]

# Pourquoi?
# C'est parce que l'objet map est aussi un GENERATEUR.
# L'optimisation lui permet de stocker les "recettes" de 
# generation, mais on peut l'instantier qu'une fois.
# NOTE: tout generateur est aussi un iterateur.


