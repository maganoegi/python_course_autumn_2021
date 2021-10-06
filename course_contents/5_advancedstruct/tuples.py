
# Tuples sont des objets IMMUTABLES 
# Donc Memory-safe et plus rapides
>>> film = ("Good Will Hunting", "Robin Williams", 
        "Matt Damon", "Ben Affleck", 1997)

# les tuples sont ITERABLES et INDEXABLES
>>> film[0]
"Good Will Hunting"

# ... peuvent etre decomposées dans variables separees
name, actor1, actor2, actor3, year = film

# mais aussi mettre les parties dans des lists..
name, *actors, year = film

# quand une valeur ne nous importe pas...
name, *actors, _ = film

# quand une fonction retourne plusieurs valeurs,
# python les met dans un tuple.
name, *actors, _ = get_random_film()

# ====== TUPLES NOMMEES ======
>>> from collections import namedtuple
>>> Student = namedtuple("Student", [
    "first_name",
    "last_name",
    "school"
])

>>> s1 = Student(
    first_name="Sergey", 
    last_name="Platonov",
    school="Nomades"
)

# tuples nommes nous permettent d'avoir:
    # liaisons clé - valeur (comme dictionnaires)
    # indexation et itération (comme lists)
    # champs (comme classes)
    # immutabilité (comme tuples)

# elles forment donc un type hyper versatil