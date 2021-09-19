
class Duck:
    def swim(self):
        print("I can swim!")
    
    def quack(self):
        print("QUAAACK!")

class RoboticDuck:
    def swim(self):
        print("I can swim, but I will break...")
    
    def quack(self):
        print("execute Q.U.A.A.A.C.K protocol !")

class Fish:
    def swim(self):
        print("I can swim!!")


def check_if_duck(animal):
    animal.quack()
    animal.swim()

>>> check_if_duck( Duck() )
"QUAAACK!"
"I can swim!"

>>> check_if_duck( RoboticDuck() )
"execute Q.U.A.A.A.C.K protocol !"
"I can swim, but I will break..."

>>> check_if_duck( Fish() )
"AttributeError: 'Fish' object has no attribute 'quack'"