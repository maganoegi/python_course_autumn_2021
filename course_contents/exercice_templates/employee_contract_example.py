
import abc
from typing import Optional


class Contract( abc.ABC ):
    """ abstract class allowing for polymorphism between different contracts """
    @abc.abstractmethod # gonna scream if it's not implemented
    def get_pay(self) -> int:
        """ bla bla do this or it wont work
        please thing of the weekend payments: CONTACT Bill from accounting """


class HourlyContract( Contract ):
    def __init__(self, pay_rate: int, hours_worked: int) -> None:
        self._pay_rate = pay_rate
        self._hours_worked = hours_worked
    
    @property
    def pay_rate(self) -> int:
        return self._pay_rate
    
    @property
    def hours_worked(self) -> int:
        return self._hours_worked
    
    def get_pay(self) -> int:
        return self.pay_rate * self.hours_worked
    

class SalariedContract( Contract ): 
    def __init__(self, monthly_salary: int) -> None:
        self._monthly_salary = monthly_salary

    @property
    def monthly_salary(self) -> int:
        return self._monthly_salary

    def get_pay(self) -> int:
        return self.monthly_salary


class Commission( abc.ABC ):
    """ abstract class for polymophism between differet commission """
    @abc.abstractmethod # gonna scream if it's not implemented
    def get_pay(self) -> int:
        """ bla bla do this or it wont work
        please thing of the weekend payments: CONTACT Bill from accounting """


class ContractCommission( Commission ):
    def __init__(self, contracts_landed: int, price_per_contract: int = 100) -> None:
        self._contracts_landed = contracts_landed
        self._price_per_contract = price_per_contract
    
    @property
    def contracts_landed(self) -> int:
        return self._contracts_landed

    @property
    def price_per_contract(self) -> int:
        return self._price_per_contract

    def get_pay(self) -> int:
        return self.contracts_landed * self.price_per_contract


class SeasonalCommision( Commission ):
    def __init__(
        self, 
        people_killed_on_highway: int, 
        pay_per_kill: int
    ) -> None:
        self._people_killed_on_highway = people_killed_on_highway
        self._pay_per_kill = pay_per_kill

    @property    
    def people_killed_on_highway(self) -> Contract:
        """ getter """
        return self._people_killed_on_highway

    @property    
    def pay_per_kill(self) -> Contract:
        """ getter """
        return self._pay_per_kill

    def get_pay(self) -> int:
        return self.people_killed_on_highway * self.pay_per_kill * 1.1


class Employee:
    def __init__(self, name: str, id: int, contract: Contract, commission: Optional[Commission] = None) -> None: 
        self._name = name
        self._id = id
        self._contract = contract
        self._commission = commission

    @property
    def name(self) -> str:
        return self._name

    @property    
    def contract(self) -> Contract:
        """ getter """
        return self._contract

    @property    
    def commission(self) -> Commission:
        """ getter """
        return self._commission

    def __str__(self) -> str:
        return f"{self.name} earned {self.compute_pay_contract()} from contract\
             and {self.compute_pay_commission()} from commission"

    def update_contract(self, new_contract: Contract) -> 'Employee':
        """
            not a setter because setters suck, but returns a new updated object 
        """
        return Employee(name=self.name, id=self.id, contract=new_contract)

    def compute_pay_commission(self) -> int:
        # BUG: sometimes transforms into float
        return self.commission.get_pay() if self.commission else 0

    def compute_pay_contract(self) -> int:
        return self.contract.get_pay()

    def compute_pay(self) -> int:
        return self.compute_pay_contract() + self.compute_pay_commission()


class FixedContract( Contract ):
    def __init__(self, duration: int, start_salary: int, increase: int) -> None:
        self._duration = duration
        self._start_salary = start_salary
        self._increase = increase

    def get_pay(self) -> int:
        return self._start_salary + self._duration * self._increase


def main() -> None:
    
    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(henry)

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", 
        id=47832, 
        contract=sarah_contract, 
        commission=sarah_commission
    )
    print(sarah)

    taonga_contract = SeasonalCommision(
        people_killed_on_highway=2, 
        pay_per_kill=100
    )
    taonga = Employee(
        "Taonga", 
        id=12345, 
        contract=henry_contract, 
    )
    print(taonga)

    juan_contract = FixedContract(duration=20, start_salary=1000, increase=20)
    juan = Employee("Juan", 1234, juan_contract)
    print(juan)


if __name__ == '__main__':
    main()



