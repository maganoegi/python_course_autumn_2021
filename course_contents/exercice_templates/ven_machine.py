
from collections import namedtuple

Client = namedtuple("Client", ["first_name", "cash", "bought_items"])

def main() -> None:

    snacks = [
        Snickers(price=120),
        Twix(price=120),
        Bounty(price=120),
        Snickers(price=120)
    ]

    drinks = [
        CocaCola(price=390),
        CocaCola(price=390),
        CocaColaLight(price=450),
        Fanta(price=120),
        Ramseier_no_bubbles(price=120)
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
    # print following statements
        # for drinks with gaz "hmm what a delicious fizzy drink"
        # for drinks without gaz "hmm what a delicious drink"
        # for snacks with 2 pieces inside a pack "thank got there are two of you"
        # for snacks with 1 piece inside a pack "yay"

    print(f"anna before buying: {anna.cash}")
    anna = VendingMachine.process_order(
        machine=snack_machine, 
        client=anna, 
        order=Fanta
    )
    print(f"anna after buying: {anna.cash}")


if __name__ =="__main__":
    # main()

    class Animal:
        def __init__(self, price):
            self._price = price
        
        @property
        def price(self):
            return self._price

        def make_noise(self):
            print("noise......")

    class Tiger( Animal ):
        def make_noise(self):
            print("Rawr")

    class Cat( Animal ):
        pass

    a = Animal(12)
    t = Tiger(13)
    c = Cat(12)

    print(type(t))

