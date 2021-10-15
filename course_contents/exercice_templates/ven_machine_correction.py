
from collections import namedtuple
from typing import List, Type, Optional
import abc

Client = namedtuple("Client", ["first_name", "cash", "bought_items"])

class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price

class Consumable:
    def consume(self):
        """ defines the consommation behavior """
        print(super().get_characteristic() + f" - {type(self).__name__}")

class ProductCaracteristic( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def get_characteristic(cls):
        """ get the characteristic proper to the child class """

class Carbonated( ProductCaracteristic ): 
    def get_characteristic(cls):
        return "carbonated drink"

class StillDrink( ProductCaracteristic ): 
    def get_characteristic(cls):
        return "still drink"

class SinglePiece( ProductCaracteristic ): 
    def get_characteristic(cls):
        return "single piece food"

class DoublePiece( ProductCaracteristic ): 
    def get_characteristic(cls):
        return "double piece food"

class Snickers( Product, Consumable, SinglePiece ): 
    def __init__(self, price):
        super().__init__(price)
    
class Twix( Product, Consumable, DoublePiece ): 
    def __init__(self, price):
        super().__init__(price)
    
class Bounty( Product, Consumable, DoublePiece ): 
    def __init__(self, price):
        super().__init__(price)
    
class CocaCola( Product, Consumable, Carbonated ): 
    def __init__(self, price):
        super().__init__(price)
    
class CocaColaLight( Product, Consumable, Carbonated ): 
    def __init__(self, price):
        super().__init__(price)
    
class Fanta( Product, Consumable, Carbonated ): 
    def __init__(self, price):
        super().__init__(price)
    
class RamseierNoBubbles( Consumable, StillDrink, Product ): 
    def __init__(self, price):
        super().__init__(price)
    
class VendingMachine:
    def __init__(
        self,
        id: int,
        contents: List[Product]
    ):
        self._id = id
        self._contents = contents

    @property
    def id(self):
        return self._id

    @property
    def contents(self):
        return self._contents

    def get_prices_by_type(self, prod_type: Type[Product]) -> List[int]:
        """ gives the list of prices of objects of a given type """
        return [p.price for p in self.contents if isinstance(p, prod_type)]

    def remove_content_if_exists(
        self, 
        prod_type: Type[Product], 
        price: int
    ) -> Optional[Product]:
        """ removes product with the price from inventory, and returns it """
        for p in self.contents:
            if isinstance(p, prod_type) and p.price == price:
                self._contents.remove(p)
                return p

    @classmethod
    def process_order(
        cls, 
        machine, 
        client: Client,
        order: Product
    ) -> Client:
        """Processes the clients order, taking cash if product is found"""
        new_bought_items = client.bought_items[:]
        targets = machine.get_prices_by_type(order)
        price_to_remove = 0
        if len(targets) != 0:
            price_to_remove = min(targets)
            new_bought_items.append(
                machine.remove_content_if_exists(
                    order,
                    price_to_remove
                )
            )

        return Client(
            first_name = client.first_name,
            cash = client.cash - price_to_remove,
            bought_items = new_bought_items 
        )

def main() -> None:
    Client = namedtuple("Client", ["first_name", "cash", "bought_items"])

    snacks = [
        Snickers(price=120),
        Twix(price=120),
        Bounty(price=120),
        Snickers(price=120)
    ]

    drinks = [
        CocaCola(price=390),
        CocaCola(price=390),
        Fanta(price=60),
        CocaColaLight(price=450),
        Fanta(price=120),
        RamseierNoBubbles(price=120)
    ]

    snack_machine = VendingMachine(id=123, contents = snacks + drinks)

    bob: namedtuple = Client(first_name="Bob", cash=2000, bought_items=[])
    anna: namedtuple = Client(first_name="Anna", cash=1000, bought_items=[])

    print(f"bob before buying: {bob.cash}")
    bob = VendingMachine.process_order(
        machine=snack_machine, 
        client=bob, 
        order=Fanta
    )
    print(f"bob after buying: {bob.cash}")

    [item.consume() for item in bob.bought_items]

    print(f"anna before buying: {anna.cash}")
    anna = VendingMachine.process_order(
        machine=snack_machine,
        client=anna, 
        order=Fanta
    )
    anna = VendingMachine.process_order(
        machine=snack_machine,
        client=anna, 
        order=Bounty
    )
    anna = VendingMachine.process_order(
        machine=snack_machine,
        client=anna, 
        order=Fanta
    )
    print(f"anna after buying: {anna.cash}")
    [item.consume() for item in anna.bought_items]

if __name__ =="__main__":
    main()