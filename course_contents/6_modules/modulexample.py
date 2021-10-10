
# importer un built-in module:
import random

>>> random.randint(0, 10)
8

# Importer custom module.

# DANS lib.py .....
def func():
    pass

def other_func():
    pass

# DANS __main__.py .....
import lib

>>> a = lib.func()


# Nous pouvons aussi importer la fonction elle-même...
from lib import other_func

>>> a = other_func()

# ainsi que la renommer...
import lib as thebestLIBever
# ou alors
from lib import other_func as the_best_f

# ATTENTION - bonne pratique:
    # évitez d'importer la fonction - importez le module.
        # rend les sources du code clair.
    
    # quand vous renommez le module avec AS
    # verifiez quels sont les noms standards
    # pour ce module.

# Pour rendre des fonctions PRIVEES, ajoutez un _
def _private_function():
    pass