

import server
import server.lib.crud as crud

@server.app.route("/")
def home():
    print("success")
    return "success"

@server.app.route("/users/add/<string:firstname>/<string:lastname>/<string:address>")
def add_user(firstname: str, lastname: str, address: str):
    return crud.insert_user(firstname, lastname, address)

@server.app.route("/users")
def get_all_users():
    return crud.get_all_users()

@server.app.route("/accounts/add/<int:accountnb>/<string:address>")
def add_account(accountnb: int, address: str):
    return crud.insert_account(accountnb, address)

@server.app.route("/accounts")
def get_all_accounts():
    return crud.get_all_accounts()