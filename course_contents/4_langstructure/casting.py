

# conversion IMPLICITE
>>> x = 12 # int
>>> y = 1.0 # float

>>> type(x * y)
float

>>> type(x % y)
float

# Pourquoi?

>>> type("Hello World" + x)
TypeError
















# conversion EXPLICITE
>>> x = 1.0
>>> y = int(x)
>>> type(y)
int

>>> str(x)
'1.0'










