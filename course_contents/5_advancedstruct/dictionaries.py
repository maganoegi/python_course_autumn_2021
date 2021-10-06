
# dictionnaires dont des structures
# de donnes avec les proprietés suivantes:
    # jeux de clé-valeur
    # garantie d'unicité de clés
    # rapidité de lookup (voir hashtable)

>>> my_dict = {
    "key_a" : "val_a",
    "key_b" : "val_b",
    "key_c" : "val_c",
}

# elles ne sont donc pas indexables ni iterables
# comme les tuples nommes.
# Leur but principal est d'assurer une valeur de clé
# unique...
>>> my_dict["key_c"]
"val_c"

# ajouter un nouveau item unique...
>>> my_dict["key_x"] = "val_x"

# ATTENTION:
#   ajour d'élément avec le meme clé 
#   va overrride l'élément
>>> my_dict["key_a"] = "another a value"

# prendre tous les clés...
>>> my_dict.keys()
dict_keys(["key_a", "key_b", "key_c"])

# prendre tous les items...
>>> my_dict.items()
dict_items([("key_a", "val_a"), (...), (...)])

# prendre toutes les valeurs
>>> my_dict.values()
dict_values([..., ..., ...])
