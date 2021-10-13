
from collections import namedtuple


def main() -> None:
    Client = namedtuple("Client", ["first_name", "cash"])

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
        Ramseier(price=120)
    ]

    snack_machine = VendingMachine(id=123, contents = snacks + drinks)

    bob: namedtuple = Client(first_name="Bob", cash=2000)
    anna: namedtuple = Client(first_name="Anna", cash=2000)

    print(f"bob before buying: {bob.cash}")
    bob = VendingMachine.process_order(client=bob, order=Fanta)
    print(f"bob after buying: {bob.cash}")

    print(f"anna before buying: {anna.cash}")
    anna = VendingMachine.process_order(client=anna, order=Fanta)
    print(f"anna after buying: {ana.cash}")


if __name__ =="__main__":
    main()