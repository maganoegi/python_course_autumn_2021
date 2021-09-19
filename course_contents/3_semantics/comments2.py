

def weird_function(y):
    """quick explanation on what the function does.
    
    A more elaborate explanation on what the function
    does. Here the algorithms can be explained, as 
    well as other details. This type of comment 
    is called a DOCSTRING.

    ARGS:
        what arguments and types to expect

    RETURNS:
        what type and what that value represents
    """

    # line comment to explain this step, 
    # if it's not clear
    x = y + 1 

    # generally, AVOID OVER-COMMENTING:
    # a variable/function name must speak for itself

    return "".join(map(lambda x : tw.indent(x, INDENT), [
        SECTION_OPEN,
        self.contents,
        SECTION_CLOSE
    ]))

