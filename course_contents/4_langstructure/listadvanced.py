
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

# Comprehension des Listes
# manière de composer des nouveaux listes
# a partir des "règles" et boucles FOR imbriquées.

# PLUS RAPIDE, "MEMORY SAFE", FACILE A LIRE
>>> lst = [0, 1, 2, 3, 4, 5, 6]
>>> lst_squared = [x**2 for x in lst]

# Qu'est-ce qu'il se passe?

# parcours de liste LST par valeur...
>>> lst_squared = [___ for x in lst]

# accès a la variable x  dans le scope...
>>> lst_squared = [x___ for x in lst]

# elevation de la variable (valeur de lst) en carré
>>> lst_squared = [x**2 for x in lst]

# NOTE: les [] autour signifient qu'on construit une liste
# et non une dictionnaire -> ce serait alors des {}

# Fonctions sur des listes...
>>> lst = [0, 1, 2, 4, 5, 6, 3]

# tri
>>> sorted_list = sorted(lst)

# reverse
>>> rev_list = reversed(lst)

# la somme de tous les elements
# ATTENTION: marche que pour objets avec + defini...
>>> total = sum(lst)



