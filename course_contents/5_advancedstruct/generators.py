
# jusqu'à maintenant nous avons appellé les objets ayant ce
# comportement les ITERATEURS. Plus etre plus specifique, ils
# s'appellent des GENERATEURS et forment un sous-type des iterateurs.

# ITERATEURS:
    # implementent les methodes __iter__() et __next__()
        # on peut donc les parcourir

# GENERATEURS
    # sont des iterateurs
    # nous donnent le contrôle sur le mémoire
        # grâce au mot-clé YIELD

def my_generator(n):
    for i in range(1, n, 2):
        yield i**3

>>> for i in my_generator(10):
...     print(i)
1
27
125
343
729

# une autre manière de créer un generateur est avec une 
# expression generatrice. Syntaxe est similaire à une 
# comprehension de liste...
>>> gen = (i**3 for i in range(1, 10, 2))
generator object

>>> list(gen)
[1, 27, 125, 343, 729]

>>>list(gen)
[]

# Quand nous utilisons une fonction pour declarer un generateur
# nous reinitialisons ce dernier à chaque fois. # TODO length
# Si on le fait avec une expression - il sera epuisé.

>>> next(my_generator)
1 
......
>>> next(my_generator)
729
>>> next(my_generator)
StopIteration error # A EVITER!

# le boucle for les capture de base, nous devons le faire nous-meme