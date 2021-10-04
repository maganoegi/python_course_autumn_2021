
# SLICING - lst[start : stop : step]
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8]

>>> lst[:]
[1, 2, 3, 4, 5, 6, 7, 8]

>>> lst[1:]
[2, 3, 4, 5, 6, 7, 8]

>>> lst[::-1] # debut à la fin avec un pas négatif
[8, 7, 6, 5, 4, 3, 2, 1]

>>> lst = "HWeolrllod"
>>> lst[::2] # pas de 2, commençant par index 0
"Hello"

>>> lst[1::2] # pas de 2, commençant par index 1
"World"

# prendre le dernier et avant-dernier element
# et additionner les deux
>>> lst = [1, 2, 3, 4, 5, 6, 7, 8]
>>> lst[-1] + lst[-2]
15
# recherche d'index...
>>> lst.index(3)
2

>>> lst.index(15)
ValueError
