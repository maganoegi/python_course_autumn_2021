

import datetime

from server.models.sql_alchemy_model import db
import abstract
from account import Account


class DataEntry( abstract.IExternalizable ):
    def __init__(
        self,
        date: datetime.date,
        expense: abstract.IExpense,
        entity: abstract.IEntity,
        account: Account
    ):
        self._date = date
        self._expense = expense
        self._entity = entity
        self._account = account

    @property
    def date(self) -> datetime.date:
        return self._date

    @property
    def expense(self) -> abstract.IExpense:
        return self._expense

    @property
    def entity(self) -> abstract.IEntity:
        return self._entity

    @property
    def account(self) -> Account:
        return self._account