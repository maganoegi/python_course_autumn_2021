import abc

class Numerical:
    @classmethod
    def choose_correct_type(cls, a: 'Numerical', b: 'Numerical') -> 'Numerical':
        return type(a) if type(a) == type(b) else Float

    def __str__(self) -> str:
        return str(self.value)

class Operation (abc.ABC):
    @classmethod
    @abc.abstractmethod
    def apply(cls, a: Numerical, b:Numerical) -> Numerical :
        """ abstract method bla BLA  """


class Integer ( Numerical ):
    def __init__(self, value: int) -> None:
        self._value = value

    @property
    def value(self) -> int:
        return self._value


class Float ( Numerical ):
    def __init__(self, value: float) -> None:
        self._value = float(value)

    @property
    def value(self) -> float:
        return self._value


class Sum( Operation ):
    @classmethod
    def apply(cls, a: Numerical, b: Numerical) -> Numerical:
        return Numerical.choose_correct_type(a, b)(a.value + b.value)


class Multiplication( Operation ):
    @classmethod
    def apply(cls, a: Numerical, b: Numerical) -> Numerical:
        return Numerical.choose_correct_type(a, b)(a.value * b.value)


class Calculator:

    @classmethod
    def do_operation(
        cls,
        op: Operation,
        a: Numerical ,
        b: Numerical
    ) -> Numerical:
        return op.apply(a, b) 


def main() -> None:
    a = Float(1)
    b = Integer(2)
    operation = Multiplication

    c = Calculator.do_operation(operation, a, b)
    print(c)

if __name__ == '__main__':
    main()