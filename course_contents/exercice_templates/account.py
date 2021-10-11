
import enum

class Brands( enum.Enum ):
    APPLE = "Apple"
    HUAWEI = "Huawei"

class Cities( enum.Enum ):
    GENEVA = "Geneva"
    MOSCOW = "Moscow"
    STSULPICE = "St. Sulpice"

class Client:
    def __init__(self, name: str, age: int, city: Cities):
        self._name = name
        self._age = age
        self._city = city
    @property
    def name(self) -> str:
        return self._name
    @property
    def age(self) -> int:
        return self._age

    def age(self) -> int:
        return self._age
        
    @property
    def city(self) -> Cities:
        return self._city
    def __str__(self) -> str:
        return f"Client {self.name}, age {self.age} lives in {self.city.value}"

class Product:
    def __init__(self, brand: Brands):
        self._brand = brand

    @property
    def brand(self):
        return self._brand

    def __str__(self):
        return self.brand.value

class Order:
    def __init__(self, client: Client, qty: int, product: Product):
        self._client = client
        self._qty = qty
        self._product = product
    
    @property
    def client(self) -> Client:
        return self._client

    @property
    def qty(self) -> int:
        return self._qty

    @property
    def product(self) -> Product:
        return self._product

    @classmethod
    def create(cls, client: Client, qty: int, product: Product):
        return Order(client, qty, product) 

    def __str__(self):
        return f"Order(client={self.client}, qty={self.qty}, product={self.product})"
    

if __name__ == '__main__':
    
    c1 = Client(name="Gerard", age=48, city=Cities.GENEVA)
    c2 = Client(name="Sergey", age=27, city=Cities.MOSCOW)
    c3 = Client(name="John", age=30, city=Cities.STSULPICE)

    apple_computer = Product(brand=Brands.APPLE)

    order = Order.create(client=c1, qty=5, product=apple_computer)

    print(order)