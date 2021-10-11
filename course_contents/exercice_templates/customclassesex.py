import enum
class Currency( enum.Enum ):
    USD = enum.auto()
    CHF = enum.auto()

class ChangeRate( enum.Enum ):
    USD_2_CHF = 1.2

class Client:

    def transfer_to(self, other, amount):
        other._amount += 1 if self.currency == other.currency else 
        other.receive(amount)
        pass

    def receive(self, amount, currency):
        self._amount += 1

if __name__ == '__main__':

    anne = Client("Anne", currency=Currency.CHF, amount=700)
    jacques = Client("Jacques", currency=Currency.USD, amount=300)

    multimat = Bancomat(total_amount=10000)

    print(anne)
    print(jacques)

    anne.transfer_to(jacques, multimat, currency=Currency.CHF, amount=500)

    print(anne)
    print(jacques)

