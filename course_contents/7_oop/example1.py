
class Person:
    def __init__(self, fname: str, age: int):
        """CONSTRUCTEUR
        
        Dicte comment un objet doit être construit.
        
        self : mot clé designe appartenance à un objet
        self._age : champ privé "_" propre à un objet
        fname & age : deux valeurs à stocker"""
        self._fname = fname
        self._age = age

    @property
    def fname(self) -> str:
        """GETTER
        
        self : mot clé designe appartenance à un objet
        self._fname : champ privé "_" propre à un objet 
        @property : lazy-loading and readability"""
        return self._fname

    @property
    def age(self) -> int:
        return self._age

    def __str__(self) -> str:
        """Built-in method override

        vue que tout en python est un objet, ils 
        contiennent deja des comportements par défaut.
        Il faut alors les "Override" - réecrire.

        Là - le comportement de transformation en string.
        
        self : mot clé designe appartenance à un objet"""
        return f"Person(fname='{self.fname}', \
                        age='{self.age}')"

    def __eq__(self, other: Person) -> bool:
        """Built-in method override

        vue que tout en python est un objet, ils 
        contiennent deja des comportements par défaut.
        Il faut alors les "Override" - réecrire.

        Là - le comportement de comparaison.

        self : mot clé designe appartenance à un objet"""
        return (
            self.fname == other.fname and 
            self.age == other.age
        )

    def say_hi(self) -> None:
        """Custom method, proper to the object (self)"""
        print(f"Hi! my name is {self.fname}!")

if __name__ == '__main__':
    mike = Person("Mike", 27)
    anna = Person(age=25, fname="Anna")

    mike.say_hi()
    anna.say_hi()

    