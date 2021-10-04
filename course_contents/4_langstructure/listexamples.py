
# initialisons une liste...
>>> lst = []

# ajoutons quelque chose...
>>> lst.append(12)
[12]

# et encore, mais de type different...
>>> lst.append("douze")
[12, "douze"]

# ATTENTION: ne faites jamais ça s'il vous plaît...
# et S'IL FAUT le faire, utilisez les TUPLES:
>>> t = (12, "douze")



# listes sont ITERABLES...
# donc on peut les parcourir par valeur
>>> for value in lst:
...     print(value) 
12
"douze"



# elles sont aussi indexables...
>>> lst[0]
12


# et on peut avoir des listes dans listes
>>> nested = [
...     ["uno", "dos", "tres"], 
...     ["eins", "zwei", "polizei"],
...     ["bonjour"]   
... ]

>>> silly_phrase = [
...     nested[2][0],
...     nested[0][1],
...     nested[1][2]
... ]

>>> " ".join(silly_phrase)
"bonjour dos polizei"



"=============="
