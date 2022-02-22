



import abc



class RealEstate( abc.ABC ):
    @abc.abstractmethod
    def do_something(self):
        """ ........ """

    @abc.abstractmethod
    def do_something_else(self):
        """ ........ """


class SwissRealEstate( RealEstate ):
    def __init__(
        self, 
        area: int = None,
        price: int = None,
        area: int = None,
        price: int = None,

        area: int = None,
        price: int = None,

        area: int = None,
        price: int = None,

        area: int = None,
        price: int = None,
        area: int = None,
        price: int = None,
        area: int = None,
        price: int = None,

        area: int = None,
        price: int = None,

        area: int = None,
        price: int = None,

        area: int = None,
        price: int = None,
    ):
        self._price = price
        self._area = area

    @property
    def price(self):
        return self._price

    @property
    def area(self):
        return self._area

    def do_something(self):
        """ ........ """

    def do_something_else(self):
        """ ........ """


class GermanRealEstate( RealEstate ):
    def __init__(
        self, 
        schnitzel_per_meter: int = None,
        price: int = None
    ):
        self._schnitzel_per_meter = schnitzel_per_meter
        self._price = price

    @property
    def price(self):
        return self._price

    @property
    def schnitzel_per_meter(self):
        return self._schnitzel_per_meter

    def add_price(self, price):
        self._price = price
        return self

    def add_schnitzels(self, qty):
        self._schnitzel_per_meter = qty
        return self

    def do_something(self):
        """ ........ """

    def do_something_else(self):
        """ ........ """


class RealEstateBuilder( abc.ABC ):
    @classmethod
    @abc.abstractmethod
    def build(cls):
        """ abstract class method allowing different build implementations """

class SwissRealEstateBuider( RealEstateBuilder ):
    @classmethod
    def build(cls, **kwarms):
        """ class method allowing swiss real estate build  """
        sre = SwissRealEstate()
        return sre.add_price().add_area()

class GermanRealEstate( RealEstateBuilder ):
    @classmethod
    def build(cls, **kwargs):
        """ class method allowing swiss real estate build  """
        sre = SwissRealEstate()
        return sre.add_price().add_schnitzels()

