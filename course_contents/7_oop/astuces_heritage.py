
# Quand une classe hétite d'une
# autre, elle reprend ces caracteristiques...
class Parent:
    def __init__(self):
        self.role = "parent"

class Child( Parent ):
    def __init__(self):
        self.role = "child"

>>> p = Parent()
>>> c = Child()
>>> p.role
"parent"
>>> c.role
"child"

# Observer ceci...
class Parent:
    def __init__(self):
        self.role = "parent"

class Child( Parent ):
    pass
