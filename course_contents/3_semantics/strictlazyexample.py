

# evaluation stricte, rien d'intéressant...
x = 0
x += sum([1, 2])

class DataBaseManager:
    ...
    # example de lazy eval ;) résultats en cache 
    
    @property 
    def all_user_accounts(self):
        # do something insanely LONG and HORRIBLE...
        return result
