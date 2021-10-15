


import abc
import enum
from typing import List, Optional

class VehicleBrand( enum.Enum ):
    AUDI = "audi"
    VW = "volkswagen"
    PORSCHE = "porsche"
    FERRARI = "ferrari"
    LADA = "lada"

class VehicleColor( enum.Enum ):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

class VehicleType( enum.Enum ):
    CAR = "car"
    BIKE = "bike"
    BUS = "bus"

class Vehicle( abc.ABC ):
    
    @abc.abstractmethod
    def drive(self) -> None:
        """abstract class defining the ability to drive"""
    
    # @abc.abstractmethod
    # def accept_passenger(self, passenger: Person) -> None:
    #     """ abstract method defining the ability to accept a passenger """

    # @abc.abstractmethod
    # def nb_passengers_acceptable(self) -> int:
    #     """returns the number of passengers that can fit inside the vehicle."""

    @property
    @abc.abstractproperty
    def brand(self) -> VehicleBrand:
        """gives us the brand of the vehicle"""
    
    @property
    @abc.abstractproperty
    def color(self) -> VehicleColor:
        """ returns the color of the vehicle """

    # @property
    # @abc.abstractproperty
    # def passengers(self) -> List[Person]:
    #     """the passengers of the vehincle """

class Car( Vehicle ):

    def __init__(
        self,
        brand: VehicleBrand,
        color: VehicleColor
    ):
        self._brand = brand
        self._color = color

    def drive(self) -> None:
        """abstract class defining the ability to drive"""
        print(f"I am driving a {self.color.value} {self.brand.value}")

    @property
    def brand(self) -> VehicleBrand:
        """gives us the brand of the vehicle"""
        return self._brand 
    
    @property
    def color(self) -> VehicleColor:
        """ returns the color of the vehicle """
        return self._color 

class Bus( Vehicle ):

    def __init__(
        self,
        brand: VehicleBrand,
        color: VehicleColor
    ):
        self._brand = brand
        self._color = color

    def drive(self) -> None:
        """abstract class defining the ability to drive"""
        print(f"I am driving a {self.color.value} {self.brand.value}")

    @property
    def brand(self) -> VehicleBrand:
        """gives us the brand of the vehicle"""
        return self._brand 
    
    @property
    def color(self) -> VehicleColor:
        """ returns the color of the vehicle """
        return self._color 

class Bike( Vehicle ):
    pass

class Factory:
    # BUG: cant use enum as a key, apparently
    type_vehicle_coupling = {
        VehicleType.BUS : Bus,
        VehicleType.BIKE : Bike,
        VehicleType.CAR : Car
    }

    @classmethod
    def create_vehicle_from(
        cls, 
        brand: str,
        color: str,
        vehicle_type: str
    ) -> Optional[Vehicle]:
        """factory class method that generates vehicle class instances.

        .........

        ARGS:
            asdasd
        
        RETURNS:
            Vehicle instance (optional)
        """

        selected_color = None
        selected_brand = None

        if brand == VehicleBrand.AUDI.value:
            selected_brand = VehicleBrand.AUDI

        elif brand == VehicleBrand.PORSCHE.value:
            selected_brand = VehicleBrand.PORSCHE

        else:
            selected_brand = VehicleBrand.LADA


        if color == VehicleColor.GREEN.value:
            selected_color = VehicleColor.GREEN

        elif color == VehicleColor.BLUE.value:
            selected_color = VehicleColor.BLUE
            
        else:
            selected_color = VehicleColor.RED


        if vehicle_type in [VehicleType.CAR.value, VehicleType.BUS.value]:
            return cls.type_vehicle_coupling[VehicleType](
                brand=selected_brand,
                color=selected_color
            )

        else:
            print("I cannot do that")  
            return None      


if __name__ == '__main__':  

    done = False

    while not done:
        brand = input("Please provide the brand:\t")
        color = input("Please provide the color:\t")
        vehicle_type = input("Please provide the type:\t")

        vehicle = Factory.create_vehicle_from(
            brand=brand, 
            color=color, 
            vehicle_type=vehicle_type
        )

        if vehicle:
            vehicle.drive() 