
# Ceci est un string...
>>> hello = "Hello"
>>> world = 'World'

# Strings peuvent subir des opérations...
>>> combined_string = hello + world
"HelloWorld"

# strings peuvent être formatées...
>>> formatted_string = f"{combined_string} misses a space..."
"HelloWorld misses a space..."

>>> list_of_strings = [
...     "hello",    
...     "world"   
... ]
>>> " ".join(list_of_strings).upper()
"hello world"

# strings peuvent être considerées comme des listes...
>>> first_char = formatted_string[0]
"H"

>>> len(first_char)
1

>>> 'Python' in formatted_string
False

# ... mais ils ont aussi des methodes propres...
>>> combined_string.upper()
'HELLOWORLD'

>>> combined_string.lower()
'helloworld'

>>> "hello world         ".strip()
"hello world"

# les '' peuvent être utilisées à l'intérieur de ""