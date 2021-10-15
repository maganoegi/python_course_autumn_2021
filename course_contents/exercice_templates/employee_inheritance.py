



import abc

class Employee( abc.ABC ):
    """Basic representation of an employee at the company."""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def compute_pay(self) -> int:
        """Compute how much the employee should be paid."""
        pass

class HourlyEmployee( Employee ):
    """Employee that's paid based on number of worked hours."""
    def __init__(
        self, 
        name: str,
        pay_rate:int, 
        hours_worked:int = 0, 
        employer_cost:int = 1000
    ):
        # self == this
        self._name = name
        self._pay_rate = pay_rate
        self._hours_worked = hours_worked
        self._employer_cost = employer_cost

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def pay_rate(self) -> int:
        return self._pay_rate

    @property
    def hours_worked(self) -> int:
        return self._hours_worked

    @property
    def employer_cost(self) -> int:
        return self._employer_cost
        
    def compute_pay(self) -> int:
        return self.pay_rate * self.hours_worked + self.employer_cost

class SalariedEmployee( Employee ):
    """Employee that's paid based on a fixed monthly salary."""
    def __init__(
        self, 
        name,
        monthly_salary:int, 
        percentage:float = 1.0, 
    ):
        self._name = name
        self._monthly_salary = monthly_salary
        self._percentage = percentage

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def monthly_salary(self) -> int:
        return self._monthly_salary

    @property
    def percentage(self) -> int:
        return self._percentage

    def compute_pay(self) -> int:
        return self.monthly_salary * self.percentage

class Freelancer( Employee ):
    """Freelancer that's paid based on number of worked hours."""
    def __init__(
        self, 
        pay_rate:int, 
        hours_worked:int = 0, 
    ):
        self._pay_rate = pay_rate
        self._hours_worked = hours_worked
    
    @property
    def pay_rate(self) -> int:
        return self._pay_rate

    @property
    def hours_worked(self) -> int:
        return self._hours_worked

    def compute_pay(self) -> int:
        return self.pay_rate * self.hours_worked

class SalariedEmployeeWithCommission( SalariedEmployee ):
    def __init__(
        self, 
        name:str,
        monthly_salary:int, 
        percentage:float = 1.0,
        commission:int = 100, 
        contracts_landed:int = 0
    ):
        super().__init__(
            monthly_salary=monthly_salary, 
            name=name, 
            percentage=percentage
        )
        self._commission = commission
        self._contracts_landed = contracts_landed

    @property
    def contracts_landed(self) -> int:
        return self._contracts_landed

    @property
    def commission(self) -> int:
        return self._commission

    def compute_pay(self) -> int:
        return super().compute_pay() + (self.commission * self.contracts_landed)

class HourlyEmployeeWithCommission(...):
    NotImplementedError
    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed

class FreelancerWithCommission( Freelancer ):
    NotImplementedError
    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed

def main() -> None:

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )

if __name__ == "__main__":
    main()
