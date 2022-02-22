

from server.models.sql_alchemy_model import db
import server.lib.classes.abstract as abstract

class UserOrm( db.Model ):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    address = db.Column(db.String(250))


class AccountOrm( db.Model ):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True) 
    account_nb = db.Column(db.Integer)
    address = db.Column(db.String(250)) 


class User( abstract.IExternalizable ):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        address: str
    ):
        self._first_name = first_name
        self._last_name = last_name
        self._address = address

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def address(self) -> str:
        return self._address

    @classmethod
    def orm_type(cls):
        return UserOrm

    def to_orm(self) -> UserOrm:
        return self.__class__.orm_type()(
            first_name=self.first_name, 
            last_name=self.last_name,
            address=self.address,
        )


class Account( abstract.IExternalizable ):
    def __init__(
        self,
        account_nb: int,
        address: str
    ):
        self._account_nb = account_nb
        self._address = address

    @property
    def account_nb(self) -> int:
        return self._account_nb

    @property
    def address(self) -> int:
        return self._address

    @classmethod
    def orm_type(cls):
        return AccountOrm

    def to_orm(self) -> AccountOrm:
        return self.__class__.orm_type()(
            account_nb=self.account_nb, 
            address=self.address
        )

