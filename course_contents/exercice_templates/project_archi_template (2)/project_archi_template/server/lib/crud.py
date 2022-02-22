
from server.models.sql_alchemy_model import db
from server.lib.classes.accounting import User, Account

def insert_user(first_name: str, last_name: str, address: str):
    user = User(first_name, last_name, address)
    db.session.begin()
    db.session.add(user.to_orm())
    db.session.commit()
    print(f"============== {user} ADDED ================")
    return "0"

def get_all_users():
    db.session.begin()
    users = db.session.query(User.orm_type()).all() 
    for user in users:
        print(user.first_name)
    return "0"

def insert_account(account_nb: int, address: str):
    account = Account(account_nb, address)
    db.session.begin()
    db.session.add(account.to_orm())
    db.session.commit()
    print(f"============== {account} ADDED ================")
    return "0"

def get_all_accounts():
    db.session.begin()
    accounts = db.session.query(Account.orm_type()).all() 
    for account in accounts:
        print(account.account_nb)
    return "0"

