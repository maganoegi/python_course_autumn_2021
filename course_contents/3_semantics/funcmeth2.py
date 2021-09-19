
# ==================================================



# en Mathématiques:     f(x) = x + 1
# en Python:            f(x) 

def f(x):
    """mot clé DEF designe une fonction. 
    Incremente de 1. 
    """
    x += 1
    return x

# appel de fonction avec ARGUMENT POSITIONNEL:
>>> output = f(1)
2







def f(x):
    """mot clé DEF designe une fonction. 
    Incremente de 1. 
    """
    x += 1
    return x

# appel de fonction sans argument réquis:
>>> output = f()
"TypeError: func() missing 1 required" 
"positional argument: x"







def f(x):
    """mot clé DEF designe une fonction. 
    Incremente de 1. 
    """
    x += 1
    return x

# appel de fonction avec ARGUMENT NOMME:
>>> output = f(x=2)
3








# fonction LAMBDA, sur une ligne
>>> l = lambda x : x + 1
>>> l(1)
2











# fonction avec nombre variable d'arguments
def sum_all(*args):
    result = 0
    for arg in args:
        result += arg
    
    return result
    
>>> output = sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9)
45













# fonction avec somme variable des variables nommées
def format_greeting(**kwargs):
    for key, value in kwargs.items():
        print("My {0} is {1}".format(key, value))

>>> format_greeting(name="Sergey")
"My name is Sergey"







# ==================================================



