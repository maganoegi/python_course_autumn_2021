
import abc
from typing import TypeVar, List

T = TypeVar("T")
V = TypeVar("V")

class IExternalizable( abc.ABC ):
    """ Abstract class allowing for ORM representation of a class """

    @classmethod
    @abc.abstractmethod
    def orm_type(cls):
        """ abstract class method for return of ORM representation class """

    @abc.abstractmethod
    def to_orm(self):
        """ abstract class method for return of ORM representation object """


class IEntity( abc.ABC ):
    """ Abstract base class for all the Entities. """


class IExpense( abc.ABC ):
    """ Abstract base class for all the Expenses. """

    @property
    @abc.abstractmethod
    def amount(self) -> int:
        """ abstract property method for cash amount information """


class IAnalysisStrategy( abc.ABC ):
    """ Abstract base class for all the Analysis Strategies. """

    @classmethod
    @abc.abstractmethod
    def apply(cls, data: List[IExpense]) -> V:
        """ abstract class method - applies the analysis strategy to input """