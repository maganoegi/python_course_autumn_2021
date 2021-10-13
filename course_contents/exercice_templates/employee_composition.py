
import abc
from typing import Optional

class Contract(abc.ABC):
    """Represents a contract anda payment process for a particular employeee."""
    @abc.abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""

class Commission( abc.ABC ):
    """Represents a commission payment process."""
    @abc.abstractmethod
    def get_payment(self) -> int:
        """Returns the commission to be paid out."""

class ContractCommission( Commission ):
    """Represents a commission payment process based on the number of contracts landed."""
    def __init__(self, commission:int = 100, contracts_landed:int = 0):
        self.commission = commission
        self.contracts_landed = contracts_landed
    
    def get_payment(self) -> int:
        """Returns the commission to be paid out."""
        return self.commission * self.contracts_landed

class Employee:
    """Basic representation of an employee at the company."""

    def __init__(
        self, 
        name : str,
        id : int,
        contract: Contract,
        commission : Optional[Commission] = None
    ):
        self.name = name
        self.id = id
        self.contract = contract
        self.commission = commission
    
    def compute_pay(self) -> int:
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout

class HourlyContract( Contract ):
    """Contract type for an employee being paid on an hourly basis."""
    def __init__(
        self, 
        pay_rate : int,
        hours_worked : int = 0,
        employer_cost: int = 1000
    ):
        self.hours_worked = hours_worked
        self.pay_rate = pay_rate
        self.employer_cost = employer_cost

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost

class SalariedContract(Contract):
    """Contract type for an employee being paid a monthly salary."""
    def __init__(
        self, 
        monthly_salary : int,
        percentage : float = 1.0,
    ):
        self.monthly_salary = monthly_salary
        self.percentage = percentage

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage

class FreelancerContract(Contract):
    """Contract type for a freelancer (paid on an hourly basis)."""

    def __init__(
        self, 
        pay_rate : int,
        hours_worked : int = 0,
    ):
        self.pay_rate = pay_rate
        self.hours_worked = hours_worked

    def get_payment(self) -> int:
        return self.pay_rate * self.hours_worked

def main() -> None:

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours "
        f"and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission
    )
    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts "
        f"and earned ${sarah.compute_pay()}."
    )

if __name__ == "__main__":
    main()
