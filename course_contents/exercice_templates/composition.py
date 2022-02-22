
import abc

class Os:
    ...

class Os( abc.ABC ):
    """ docstring """
    @classmethod
    @abc.abstractmethod
    def turn_on(cls):
        """ another docstring """

class Mac( Os ):
    ON_CODE = 0

    @classmethod
    def turn_on(cls):
        return cls.ON_CODE

class Windows( Os ):
    ON_CODE = 1

    @classmethod
    def turn_on(cls):
        return cls.ON_CODE



class PaymentMethod( abc.ABC ):
    """ docstring """
    @classmethod
    @abc.abstractmethod
    def calculate_change(cls, amount, price):
        """ another docstring """

class Cash( PaymentMethod ):
    @classmethod
    def calculate_change(cls, amount, price) -> int:
        return amount - price

class Card( PaymentMethod ):
    @classmethod
    def calculate_change(cls, amount, price) -> int:
        return amount - price / 2

class Twint( PaymentMethod ):
    @classmethod
    def calculate_change(cls, amount, price) -> int:
        return amount - price * 2



class VendingMachine:
    def __init__(self, payment_method: PaymentMethod, os: Os):
        self._payment_method = payment_method
        self.os = os
        self.status_code = None

    def accept_payment(self, amount) -> int:
        return self._payment_method.calculate_change(amount, 10)

    def turn_on(self):
        self._os.turn_on()

    def is_on(self):
        return self.status_code != None and self.status_code == self._os.ON_CODE

if __name__ == '__main__':
    
    content_basket = []

    # fill the vending machine
    machine_chj1 = VendingMachine().fill_with(content_basket)

    machine_chj1.turn_on()

    while machine_chj1.is_on():
        # get user input on the selection
        user_input_string = input("what would you like to buy? ")

        try:
            position = int(user_input_string)
        
        except ValueError:
            print("please dont mess wiht me ")
            continue

        is_contained = machine_chj1.contains_at_position(position)
        if is_contained:
            change = machine_chj1.accept_payment(1000)

    # retrieve what we want, provided it's inside the machine



    # consume the product