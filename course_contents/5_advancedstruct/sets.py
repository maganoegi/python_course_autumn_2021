
# d'après la théorie des ensembles en maths
# (SET THEORY), nous avons aussi le type set...
>>> my_set = {1, 2, 3, 4, 5}

# la particularité de ce type est l'unicité des valeurs
# ainsi que les caracteristiques se SET Theory:
>>> s1 = {1, 2, 3}
>>> s2 = {1, 2}
>>> s3 = {4, 5, 6}

>>> s2 <= s1
True # car s2 est un sous-ensemble de s1
>>> s2 <= s3
False # car s2 n'est pas un sous-ensemble de s3