



# class Consumable:
#     def __init__(self, origin):
#         print("initilalizing Consumable")
#         self.origin = origin

# class Beverage( Consumable ):
#     def __init__(self, water_percentage, origin):
#         super().__init__(origin)
#         print("initilalizing Beverage")
#         self.water_percentage = water_percentage


# class AlcoholicBeverage( Beverage ):
#     def __init__(self, alcohol_percentage, water_percentage, origin):
#         super().__init__(water_percentage, origin)
#         print("initilalizing AlcoholicBeverage")
#         self.alcohol_percentage = alcohol_percentage

# class Beer( AlcoholicBeverage ):
#     def __init__(self, brand, alcohol_percentage, water_percentage, origin):
#         super().__init__(alcohol_percentage, water_percentage, origin)
#         print("initilalizing Beer")
#         self.brand = brand


class Consumable:
    def consume(self):
        print("nom nom nom...")


class Fuzzy:
    def sparkle(self):
        print("brr brr brr")


class ContainsAlcohol:
    def intoxicate(self):
        print("%&/(%*/&")
    # ...
    # pass
    # """ docstring """
    # raise NotImplementedError


class NotForKids:
    def can_be_sold(self):
        print("NO !")


class Beer( Consumable, Fuzzy, ContainsAlcohol, NotForKids ):
    ...


class Humanoid:
    ...

class CanSwim:
    def swim(self):
        if isinstance(self, Humanoid):
            if self.has_unlocked_swimming:
                print("logic on how to swim")
            else:
                print("logic on how to die")
        
        else:
            print("I dont know how but i am swimming")

class PlayerCharacter( CanSwim, Humanoid ):
    def __init__(self, level, has_unlocked_swimming):
        self.level = level
        self.has_unlocked_swimming = has_unlocked_swimming

class NPC( CanSwim, Humanoid ):
    ...

class Vehicle( CanSwim ):
    ...

class Dragon( Vehicle ):
    ...



if __name__ == '__main__':
    a_cold_one = PlayerCharacter(2, True)
    a_cold_one.swim()



# hier: composition             dependance: minimale, code-reuse: minimal, protection: maximale
# cas extreme de heritage       dependance: maximale, code-reuse: maximale, protection: aucune
# cas extreme d'interfaçage     dependance: acceptable, code-reuse: depend, protection: grande (en fonction de code reuse)